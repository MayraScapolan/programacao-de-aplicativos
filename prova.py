import sqlite3

banco = sqlite3.connect("distribuidora.db")
banco.execute("PRAGMA foreign_keys = ON")


def criar_tabelas():
    try:
        banco.execute("""
            CREATE TABLE IF NOT EXISTS fabricantes_marcas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_fabricante TEXT NOT NULL,
                cnpj TEXT NOT NULL
            )
        """)
        banco.execute("""
            CREATE TABLE IF NOT EXISTS centros_distribuicao(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cidade_polo TEXT NOT NULL,
                id_fabricante INTEGER NOT NULL,
                FOREIGN KEY(id_fabricante) REFERENCES fabricantes_marcas(id)
            )
        """)
        banco.commit()
    except sqlite3.Error as erro:
        print("Erro:", erro)


def cadastrar_fabricante():
    try:
        nome = input("Fabricante: ")
        cnpj = input("CNPJ: ")
        if not nome or not cnpj:
            print("Preencha os campos.")
            return
        banco.execute(
            "INSERT INTO fabricantes_marcas(nome_fabricante,cnpj) VALUES(?,?)",
            (nome, cnpj))
        banco.commit()
        print("Cadastrado!")
    except Exception as erro:
        print("Erro:", erro)


def listar_fabricantes():
    try:
        dados = banco.execute("SELECT * FROM fabricantes_marcas").fetchall()
        for x in dados:
            print(f"ID: {x[0]} | Fabricante: {x[1]} | CNPJ: {x[2]}")
        if not dados:
            print("Nenhum fabricante cadastrado.")
    except Exception as erro:
        print("Erro:", erro)


def atualizar_fabricante():
    try:
        id = int(input("ID: "))
        nome = input("Novo fabricante: ")
        cnpj = input("Novo CNPJ: ")
        c = banco.execute(
            "UPDATE fabricantes_marcas SET nome_fabricante=?,cnpj=? WHERE id=?",
            (nome, cnpj, id))
        banco.commit()
        print("Atualizado!" if c.rowcount else "ID não encontrado.")
    except Exception as erro:
        print("Erro:", erro)


def excluir_fabricante():
    try:
        id = int(input("ID: "))
        if banco.execute(
            "SELECT id FROM centros_distribuicao WHERE id_fabricante=?",
            (id,)).fetchone():
            print("Fabricante possui centros vinculados.")
            return
        c = banco.execute(
            "DELETE FROM fabricantes_marcas WHERE id=?", (id,))
        banco.commit()
        print("Excluído!" if c.rowcount else "ID não encontrado.")
    except Exception as erro:
        print("Erro:", erro)


def cadastrar_centro():
    try:
        cidade = input("Cidade polo: ")
        fabricante = int(input("ID do fabricante: "))

        if not banco.execute(
            "SELECT id FROM fabricantes_marcas WHERE id=?", (fabricante,)
        ).fetchone():
            print("Fabricante não existe.")
            return

        banco.execute(
            "INSERT INTO centros_distribuicao(cidade_polo,id_fabricante) VALUES(?,?)",
            (cidade, fabricante))
        banco.commit()
        print("Cadastrado!")
    except Exception as erro:
        print("Erro:", erro)


def listar_centros():
    try:
        dados = banco.execute("""
            SELECT c.id,c.cidade_polo,f.nome_fabricante
            FROM centros_distribuicao c
            JOIN fabricantes_marcas f ON c.id_fabricante=f.id
        """).fetchall()

        for x in dados:
            print(f"ID: {x[0]} | Cidade: {x[1]} | Fabricante: {x[2]}")

        if not dados:
            print("Nenhum centro cadastrado.")
    except Exception as erro:
        print("Erro:", erro)


def atualizar_centro():
    try:
        id = int(input("ID do centro: "))
        cidade = input("Nova cidade: ")
        fabricante = int(input("Novo ID do fabricante: "))

        if not banco.execute(
            "SELECT id FROM fabricantes_marcas WHERE id=?", (fabricante,)
        ).fetchone():
            print("Fabricante não existe.")
            return

        c = banco.execute("""
            UPDATE centros_distribuicao
            SET cidade_polo=?,id_fabricante=?
            WHERE id=?
        """, (cidade, fabricante, id))

        banco.commit()
        print("Atualizado!" if c.rowcount else "ID não encontrado.")
    except Exception as erro:
        print("Erro:", erro)


def excluir_centro():
    try:
        id = int(input("ID do centro: "))
        c = banco.execute(
            "DELETE FROM centros_distribuicao WHERE id=?", (id,))
        banco.commit()
        print("Excluído!" if c.rowcount else "ID não encontrado.")
    except Exception as erro:
        print("Erro:", erro)