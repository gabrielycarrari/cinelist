from fastapi import Depends, FastAPI
from fastapi.staticfiles import StaticFiles
from repositories.cliente_repo import ClienteRepo
from repositories.filme_repo import FilmeRepo
from repositories.genero_repo import GeneroRepo
from repositories.item_pedido_repo import ItemPedidoRepo
from repositories.pedido_repo import PedidoRepo
from repositories.produto_repo import ProdutoRepo
from routes import main_routes, cliente_routes
from util.auth import checar_permissao, middleware_autenticacao
from util.exceptions import configurar_excecoes

# ProdutoRepo.criar_tabela()
# ProdutoRepo.inserir_produtos_json("sql/produtos.json")
GeneroRepo.criar_tabela()
GeneroRepo.inserir_generos_json("sql/generos.json")
ClienteRepo.criar_tabela()
FilmeRepo.criar_tabela()


app = FastAPI(dependencies=[Depends(checar_permissao)])
app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.middleware(middleware_type="http")(middleware_autenticacao)
configurar_excecoes(app)
app.include_router(main_routes.router)
app.include_router(cliente_routes.router)
