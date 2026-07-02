import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connct('sistema_escola.db')
    cursor = conexao.cursor()
#O aluno tenta cadastrar uma serie com id_escola =999 (qu nao existe).
#O sqlite aceita o cadastro mesmo assim. O que esta faltando ativar?
try:
    cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
(nome_serie, id_escola))
    conexao.commit()
except sqlite3.IntegrityError:
    print("Erro: Escola inexistente!")
finally:
    conexao.close()



        # Erro: faltou ativar o cursor.execute("PRAGMA foreign_keys = ON;")
#correto


import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()


    try:

        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
        (nome_serie, id_escola))
                    
        conexao.commit()
    except sqlite3.IntegrityError:
        print("Erro: Escola inexistente!")
    finally:
        conexao.close()