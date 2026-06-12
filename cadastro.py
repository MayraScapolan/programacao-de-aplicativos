import sqlite3 #Importa o SQLite para trabalhar com banco de dados.

conexao = sqlite3.connect('escola.db') #Conecta ao banco escola.db.
cursor = conexao.cursor() #O cursor é responsável por executar comandos SQL no banco de dados.
cursor.execute(''' 
      CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        turma TEXT,
        idade INTEGER,
        cpf TEXT UNIQUE NOT NULL
    )''') #Executa um comando SQL para criar a tabela alunos caso ela ainda não exista.

nome_aluno = input("NOME: ") #Pede ao usuário que digite o nome.
telefone_aluno = input("TELEFONE: ") #Pede o telefone.
turma_aluno = input("TURMA: ") #Pede a turma.
idade_aluno = int(input("IDADE: ")) #Pede a idade e converte o valor para inteiro usando int().
CPF_aluno = input("CPF: ") #Pede o CPF.

comando_inserir = (f'''
                        insert  into alunos (nome, telefone, turma, idade,cpf)
                        values('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{CPF_aluno}' )
                        ''') #A letra f antes das aspas indica uma F-String, ela substitui as variáveis pelos valores digitados pelo usuário.
                        
cursor.execute(comando_inserir) #Envia o comando SQL para o banco de dados e cadastra o aluno.
conexao.close #Fecha a conexão com o banco de dados para liberar recursos. 

#listar

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()
cursor.execute(''' select * from alunos ''')
alunos = cursor.fetchall()
if not alunos:
    print("nenhum aluno cadastrado")
else:
    for aluno in alunos:
        print(f"nome = {aluno[0]}, idade = {aluno[1]}")
conexao.close()