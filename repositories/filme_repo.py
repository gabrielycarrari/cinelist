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

    @classmethod
    def inserir(cls, filme: Filme) -> Optional[Filme]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_INSERIR, (
                    filme.nome,
                    filme.sinopse,
                    filme.id_genero,
                    filme.id_cliente,
                    filme.avaliacao
                ))
                if cursor.rowcount > 0:
                    filme.id = cursor.lastrowid
                    return filme
        except sqlite3.Error as ex:
            print(ex)
            return None
    
    
    @classmethod
    def alterar(cls, filme: Filme) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(
                    SQL_ALTERAR,
                    (
                        filme.nome,
                        filme.sinopse,
                        filme.id_genero,
                        filme.id_cliente,
                        filme.avaliacao,
                        filme.id,
                    ),
                )
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False
        
        
    @classmethod
    def excluir(cls, id: int) -> bool:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                cursor.execute(SQL_EXCLUIR, (id,))
                return cursor.rowcount > 0
        except sqlite3.Error as ex:
            print(ex)
            return False
        
    @classmethod
    def obter_por_cliente(cls, id_cliente) -> List[Filme]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tuplas = cursor.execute(SQL_OBTER_POR_CLIENTE,(id_cliente,)).fetchall()
                filmes = [Filme(*t) for t in tuplas]
                return filmes
        except sqlite3.Error as ex:
            print(ex)
            return None

    @classmethod
    def obter_por_id(cls, id: int) -> Optional[Filme]:
        try:
            with obter_conexao() as conexao:
                cursor = conexao.cursor()
                tupla = cursor.execute(SQL_OBTER_UM, (id,)).fetchone()
                if tupla is None:
                    return None
                filme = Filme(*tupla)
                return filme
        except sqlite3.Error as ex:
            print(ex)
            return None
        
    