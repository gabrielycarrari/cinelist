SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS cliente (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL,
        token TEXT)
"""

SQL_INSERIR = """
    INSERT INTO cliente(nome, email, senha)
    VALUES (?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, email, senha
    FROM cliente
    ORDER BY nome
"""

SQL_ALTERAR = """
    UPDATE cliente
    SET nome=?, email=?
    WHERE id=?
"""

SQL_ALTERAR_TOKEN = """
    UPDATE cliente
    SET token=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM cliente    
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT id, nome, email
    FROM cliente
    WHERE id=?
"""

SQL_OBTER_POR_EMAIL = """
    SELECT id, nome, email, senha
    FROM cliente
    WHERE email=?
"""

SQL_OBTER_POR_TOKEN = """
    SELECT id, nome, email
    FROM cliente
    WHERE token=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM cliente
"""

SQL_OBTER_BUSCA = """
    SELECT id, nome, email
    FROM cliente
    WHERE nome LIKE ? OR cpf LIKE ?
    ORDER BY nome
    LIMIT ? OFFSET ?
"""

SQL_OBTER_QUANTIDADE_BUSCA = """
    SELECT COUNT(*) FROM cliente
    WHERE nome LIKE ? OR cpf LIKE ?
"""


SQL_ALTERAR_SENHA = """
    UPDATE cliente
    SET senha=?
    WHERE id=?
"""