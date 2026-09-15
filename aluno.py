def listar_alunos():
    conexao = sqlite3.connect("escola.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos ORDER BY nome ASC")

    alunos = cursor.fetchall()

    for aluno in alunos:
        print(aluno)

    conexao.close()


#Ao executar o menu.py e escolher a opção de listar alunos, os registros já aparecerão ordenados alfabeticamente.