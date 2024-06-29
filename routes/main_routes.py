import math
from sqlite3 import DatabaseError
from fastapi import APIRouter, HTTPException, Query, Request, status
from fastapi.responses import HTMLResponse, JSONResponse

from dtos.entrar_dto import EntrarDTO
from dtos.novo_filme_dto import NovoFilmeDTO
from models.filme_model import Filme
from repositories.filme_repo import FilmeRepo
from repositories.genero_repo import GeneroRepo
from util.html import ler_html
from dtos.novo_cliente_dto import NovoClienteDTO
from models.cliente_model import Cliente
from repositories.cliente_repo import ClienteRepo
from util.auth import (
    conferir_senha,
    gerar_token,
    obter_hash_senha,
)

from util.cookies import adicionar_cookie_auth, adicionar_mensagem_erro, adicionar_mensagem_sucesso
from util.pydantic import create_validation_errors
from util.templates import obter_jinja_templates

router = APIRouter()
templates = obter_jinja_templates("templates/main")


@router.get("/html/{arquivo}")
async def get_html(arquivo: str):
    response = HTMLResponse(ler_html(arquivo))
    return response


@router.get("/")
async def get_root(request: Request):
    return templates.TemplateResponse(
        "pages/entrar.html",
        {
            "request": request,
        },
    )


@router.get("/sobre")
async def get_sobre(request: Request):
    return templates.TemplateResponse(
        "pages/sobre.html",
        {"request": request},
    )

@router.get("/cadastro_filme")
async def get_cadastro(request: Request):
    generos = GeneroRepo.obter_todos()
    return templates.TemplateResponse(
        "pages/cadastro_filme.html",
        {
            "request": request,
            "generos": generos,
        },
    )


@router.get("/filmes")
async def get_contato(request: Request):
    filmes = FilmeRepo.obter_por_cliente(request.state.cliente.id)
    lista_generos = GeneroRepo.obter_todos()
    generos = {genero.id: genero for genero in lista_generos}
    return templates.TemplateResponse(
        "pages/lista_filmes.html",
        {
            "request": request,
            "filmes": filmes,
            "generos": generos,
            },
    )

@router.post("/post_filme", response_class=JSONResponse)
async def post_filme(filme_dto: NovoFilmeDTO, request: Request):
    id_cliente = request.state.cliente.id

    if not GeneroRepo.obter_por_id(filme_dto.id_genero):
        raise HTTPException(status_code=400, detail="Gênero não encontrado.")

    filme_data = filme_dto.model_dump()
    filme_data['id_cliente'] = id_cliente

    novo_filme = FilmeRepo.inserir(Filme(**filme_data))
    if not novo_filme or not novo_filme.id:
        raise HTTPException(status_code=400, detail="Erro ao cadastrar filme.")
    
    response = JSONResponse(content={"redirect": {"url": "/filmes"}})
    adicionar_mensagem_sucesso(
        response,
        f"Filme <b>{novo_filme.nome}</b> cadastrado com sucesso!",
    )
    return response


@router.delete("/delete_filme/{id:int}", response_class=JSONResponse)
async def delete_filme(id: int):
    filme = FilmeRepo.obter_por_id(id)
    if not filme or not filme.id:
        raise HTTPException(status_code=400, detail="Filme não encontrado.")

    if not FilmeRepo.excluir(id):
        raise HTTPException(status_code=400, detail="Erro ao excluir filme.")
   
    response = JSONResponse(content={"redirect": {"url": "/filmes"}})
    adicionar_mensagem_sucesso(
        response,
        f"Filme <b>{filme.nome}</b> deletado com sucesso!",
    )
    print(response)
    return response


@router.get("/alterar_filme/{id}")
async def get_cadastro(request: Request, id: int):
    lista_generos = GeneroRepo.obter_todos()
    generos = {genero.id: genero for genero in lista_generos}
    filme = FilmeRepo.obter_por_id(id)
    return templates.TemplateResponse(
        "pages/alterar_filme.html",
        {
            "request": request,
            "filme": filme,
            "generos": generos,
        },
    )

@router.post("/post_alterar_filme/{id}", response_class=JSONResponse)
async def post_alterar_filme(request: Request, filme_dto: NovoFilmeDTO, id: int):
    if not GeneroRepo.obter_por_id(filme_dto.id_genero):
        raise HTTPException(status_code=400, detail="Gênero não encontrado.")
    
    filme_data = filme_dto.model_dump()
    id_cliente = request.state.cliente.id
    filme_data['id_cliente'] = id_cliente
    response = JSONResponse({"redirect": {"url": "/filmes"}})
    if FilmeRepo.alterar(Filme(id, **filme_data)):
        adicionar_mensagem_sucesso(response, "Filme alterado com sucesso!")
    else:
        adicionar_mensagem_erro(
            response, "Não foi possível alterar os dados do filme!"
        )
    return response


@router.get("/cadastro")
async def get_cadastro(request: Request):
    return templates.TemplateResponse(
        "pages/cadastro.html",
        {"request": request},
    )


@router.post("/post_cadastro", response_class=JSONResponse)
async def post_cadastro(cliente_dto: NovoClienteDTO):
    cliente_data = cliente_dto.model_dump(exclude={"confirmacao_senha"})
    cliente_data["senha"] = obter_hash_senha(cliente_data["senha"])
    novo_cliente = ClienteRepo.inserir(Cliente(**cliente_data))
    if not novo_cliente or not novo_cliente.id:
        raise HTTPException(status_code=400, detail="Erro ao cadastrar cliente.")
    return {"redirect": {"url": "/cadastro_realizado"}}


@router.get("/cadastro_realizado")
async def get_cadastro_realizado(request: Request):
    return templates.TemplateResponse(
        "pages/cadastro_confirmado.html",
        {"request": request},
    )


@router.get("/entrar")
async def get_entrar(
    request: Request,
    return_url: str = Query("/"),
):
    return templates.TemplateResponse(
        "pages/entrar.html",
        {
            "request": request,
            "return_url": return_url,
        },
    )


@router.post("/post_entrar", response_class=JSONResponse)
async def post_entrar(entrar_dto: EntrarDTO):
    cliente_entrou = ClienteRepo.obter_por_email(entrar_dto.email)
    if (
        (not cliente_entrou)
        or (not cliente_entrou.senha)
        or (not conferir_senha(entrar_dto.senha, cliente_entrou.senha))
    ):
        return JSONResponse(
            content=create_validation_errors(
                entrar_dto,
                ["email", "senha"],
                ["Credenciais inválidas.", "Credenciais inválidas."],
            ),
            status_code=status.HTTP_404_NOT_FOUND,
        )
    token = gerar_token()
    if not ClienteRepo.alterar_token(cliente_entrou.id, token):
        raise DatabaseError(
            "Não foi possível alterar o token do cliente no banco de dados."
        )
    # response = JSONResponse(content={"redirect": {"url": entrar_dto.return_url}})
    response = JSONResponse(content={"redirect": {"url": "/filmes"}})
    adicionar_mensagem_sucesso(
        response,
        f"Olá, <b>{cliente_entrou.nome}</b>. Seja bem-vindo(a) ao CineList!",
    )
    adicionar_cookie_auth(response, token)
    return response