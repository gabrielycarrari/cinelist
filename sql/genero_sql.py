SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS genero (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
       )
"""

SQL_INSERIR = """
    INSERT INTO genero(nome)
    VALUES (?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome
    FROM genero
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE genero
    SET nome=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM genero    
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT id, nome
    FROM genero
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM genero
"""

SQL_OBTER_BUSCA = """
    SELECT id, nome
    FROM genero
    WHERE nome LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM genero
    WHERE nome LIKE ?
"""
