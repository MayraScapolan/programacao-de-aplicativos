import sqlite3
def criar_tabela_turma():
    conexao = sqlite.connect('sistema_escola.db')
    cursor = conexao.cursor()
    # o SQLite acusa erro de sintaxe próximo ao FOREING KEY. cade o erro?
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomr_turma TEXT, 
            id_serie,
            FOREIGN KEY (id_serie) REFERENCES serie(id)
        )
    ''')
    conexao.commmit()
    conexao.close()

# Erro: a coluna id_serie não tinha um tipo definido para guardar o ID da série.


#correto

import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT,
            id_serie INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id)
        )
    ''')

    conexao.commit()
    conexao.close()