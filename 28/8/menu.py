import sqlite3

def conectar():
    return sqlite3.connect("gestao_escolar.db")


def menu(tabela):
    while True:
        print(f"\n--- {tabela.upper()} ---")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Alterar")
        print("4 - Excluir")
        print("5 - Voltar")

        op = input("Opção: ")
        con = conectar()
        cur = con.cursor()

        if op == "1":
            if tabela == "escolas":
                nome = input("Nome: ")
                cidade = input("Cidade: ")
                cur.execute(
                    "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
                    (nome, cidade)
                )

            elif tabela == "turmas":
                nome = input("Nome: ")
                cidade = input("Cidade: ")
                cur.execute(
                    "INSERT INTO turmas (nome, cidade) VALUES (?, ?)",
                    (nome, cidade)
                )

            else:
                nome = input("Nome: ")
                idade = int(input("Idade: "))
                turma = int(input("ID da turma: "))
                cur.execute(
                    "INSERT INTO alunos (nome, idade, id_turma) VALUES (?, ?, ?)",
                    (nome, idade, turma)
                )

        elif op == "2":
            cur.execute(f"SELECT * FROM {tabela}")
            for item in cur.fetchall():
                print(item)

        elif op == "3":
            id = input("ID: ")

            if tabela == "escolas" or tabela == "turmas":
                nome = input("Novo nome: ")
                cidade = input("Nova cidade: ")
                cur.execute(
                    f"UPDATE {tabela} SET nome=?, cidade=? WHERE id=?",
                    (nome, cidade, id)
                )
            else:
                nome = input("Novo nome: ")
                idade = int(input("Nova idade: "))
                turma = int(input("Novo ID da turma: "))
                cur.execute(
                    "UPDATE alunos SET nome=?, idade=?, id_turma=? WHERE id=?",
                    (nome, idade, turma, id)
                )

        elif op == "4":
            id = input("ID: ")
            cur.execute(f"DELETE FROM {tabela} WHERE id=?", (id,))

        elif op == "5":
            con.close()
            break

        con.commit()
        con.close()


while True:
    print("\n=== GESTÃO ESCOLAR ===")
    print("1 - Escolas")
    print("2 - Turmas")
    print("3 - Alunos")
    print("4 - Sair")

    op = input("Opção: ")

    if op == "1":
        menu("escolas")
    elif op == "2":
        menu("turmas")
    elif op == "3":
        menu("alunos")
    elif op == "4":
        break
    else:
        print("Opção inválida!")
