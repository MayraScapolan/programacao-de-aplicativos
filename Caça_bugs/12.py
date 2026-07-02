import sqlite3

# o aluno criou a conexão fora das funções para "facilitar"
# pq isso quebra o sistema quando usamos múltiplos arquivos (módulos)?
conexao = sqlite3.connect('sistema_escola.db')
cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,))
conexao.commit()

def inserir_escola(nome):
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,))
    conexao.commit()
    
# Erro: a conexão deve ser criada dentro da função para evitar problemas em projetos com vários módulos.

#correto

def inserir_escola(nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("INSERT INTO escolas(nome) VALUES (?)", (nome,))
    conexao.commit()
    conexao.close()