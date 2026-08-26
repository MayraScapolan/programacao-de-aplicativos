import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')

cursor.execute('''
                    ALTER TABLE professores ADD COLUMN endereço_professor



''')

conexao.commit()
conexao.close()