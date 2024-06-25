SQL_CRIAR_TABELA = """
    CREATE TABLE IF NOT EXISTS filme (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sinopse TEXT NOT NULL,
        id_genero INTEGER,
        id_cliente INTEGER,
        avaliacao TEXT NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES cliente(id),
        FOREIGN KEY (id_genero) REFERENCES genero(id)
    )
"""


SQL_INSERIR = """
    INSERT INTO filme(nome, sinopse, id_genero, id_cliente, avaliacao)
    VALUES (?, ?, ?, ?, ?)
"""

SQL_OBTER_TODOS = """
    SELECT id, nome, sinopse, id_genero, id_cliente, avaliacao
    FROM filme LEFT JOIN cliente ON id_cliente = cliente.id
"""

SQL_ALTERAR = """
    UPDATE filme
    SET nome=?, sinopse=?, id_genero=?, id_cliente=?, avaliacao=?
    WHERE id=?
"""

SQL_EXCLUIR = """
    DELETE FROM filme    
    WHERE id=?
"""

SQL_OBTER_UM = """
    SELECT  id, nome, sinopse, id_genero, id_cliente, avaliacao
    FROM filme LEFT JOIN cliente ON id_cliente = cliente.id
    WHERE id=?
"""

SQL_OBTER_QUANTIDADE = """
    SELECT COUNT(*) FROM filme
"""

SQL_OBTER_POR_CLIENTE = """
    SELECT id, nome, sinopse, id_genero, id_cliente, avaliacao
    FROM filme
    WHERE (id_cliente = ?)
    ORDER BY id DESC
"""