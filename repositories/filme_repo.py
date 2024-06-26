import json
import sqlite3
from typing import List, Optional
from models.filme_model import Filme
from sql.filme_sql import *
from util.database import obter_conexao


class FilmeRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)


#     @classmethod
#     def inserir(cls, filme: Filme) -> Optional[Filme]:
#         try:
#             with obter_conexao() as conexao:
#                 cursor = conexao.cursor()
#                 cursor.execute(SQL_INSERIR, (
#                     produto.nome,
#                     produto.preco,
#                     produto.descricao,
#                     produto.estoque
#                 ))
#                 if cursor.rowcount > 0:
#                     produto.id = cursor.lastrowid
#                     return produto
#         except sqlite3.Error as ex:
#             print(ex)
#             return None
