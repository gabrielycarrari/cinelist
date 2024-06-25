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

