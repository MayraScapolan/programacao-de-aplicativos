import sqlite3

def verificar_registro():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conxao.cursor()

    cursor.execute("SELECT * FROM alunos")

#Por que o segundo print não mostra absolutamente nada no console?
print("Primeiro print: " , cursor fetchall())
print("Segundo print: " , cursor fetchall())

conexao.close()