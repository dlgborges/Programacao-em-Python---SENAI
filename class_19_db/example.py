import sqlite3

#CRUD
#Create - Read - Update - Delete

con = sqlite3.connect('C:/Users/Aluno/Downloads/Programacao-em-Python---SENAI/class_19_db/example.db')

c = con.cursor()

c.execute('''
            CREATE TABLE IF NOT EXISTS tabela(
          nome TEXT,
          idade INTEGER
          )
''')

c.execute("INSERT INTO tabela VALUES(?,?)", ('Julia', 40))

con.commit()

con.close()

#C:\Users\Aluno\Downloads\Programacao-em-Python---SENAI\banco.db