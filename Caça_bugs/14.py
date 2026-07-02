import sqlite3 

def cadastrar_serue_segundo(nome, id_escola):
    try:
        #se a linha abaixo falhar por falta de permissão na pasta,
        #o bloco 'finally' vai tentar fechar algo que não abriu. como corrigir?
        conexao = sqlite3.connect('/pasta/sistema.db')
        cursor = conexao.cursor()
        cusor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)", (nome, id_escola))
        conexao.commit()
        except sqlite3.Error as e:
            print("erro tecnico:", e)
        finally:
            conexao.close()
            

# Erro: se a conexão falhar, ela não existe e o finally tenta fechar algo que não foi criado.

#correto

import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None

    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()

        cursor.execute(
            "INSERT INTO series (nome_serie, id_escola) VALUES (?,?)",
            (nome, id_escola)
        )

        conexao.commit()

    except sqlite3.Error as e:
        print("Erro técnico:", e)

    finally:
        if conexao:
            conexao.close()