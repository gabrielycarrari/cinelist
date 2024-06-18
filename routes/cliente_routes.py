from fastapi import APIRouter, Depends, Request, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from models.cliente_model import Cliente
from repositories.cliente_repo import ClienteRepo
from util.auth import checar_autorizacao, obter_cliente_logado
from util.cookies import adicionar_mensagem_sucesso


router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/pedidos")
def get_root(request: Request, cliente_logado: Cliente = Depends(obter_cliente_logado)):
    checar_autorizacao(cliente_logado)
    return templates.TemplateResponse("pedidos.html", {"request": request})


@router.get("/perfil")
def get_root(request: Request, cliente_logado: Cliente = Depends(obter_cliente_logado)):
    checar_autorizacao(cliente_logado)
    return templates.TemplateResponse("perfil.html", {"request": request})


@router.get("/sair", response_class=RedirectResponse)
async def get_sair(
    request: Request, cliente_logado: Cliente = Depends(obter_cliente_logado)
):
    checar_autorizacao(cliente_logado)
    if cliente_logado:
        ClienteRepo.alterar_token(cliente_logado.email, "")
    response = RedirectResponse("/", status.HTTP_303_SEE_OTHER)
    response.set_cookie(key="auth_token", value=" ", httponly=True, expires=0)
    adicionar_mensagem_sucesso(response, "Saída realizada com sucesso.")
    return response
