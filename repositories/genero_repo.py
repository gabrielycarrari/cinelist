import json
import sqlite3
from typing import List, Optional
from models.genero_model import Genero
from sql.genero_sql import *
from util.database import obter_conexao


class GeneroRepo:

    @classmethod
    def criar_tabela(cls):
        with obter_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CRIAR_TABELA)

