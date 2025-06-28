import sqlite3
import conexao_bd

conn = conexao_bd.conecta_bd()

def addDisciplina(disciplinaId,nome,nota1,nota2):
    try:
        declaracao = "INSERT INTO disciplina_aluno (id, nome, nota1, nota2) VALUES (?, ?, ?, ?)"
        cur = conn.cursor()
        cur.execute(declaracao, (disciplinaId, nome, nota1, nota2))
        conn.commit()
    except sqlite3.IntegrityError:
        print("\n Erro: Ja existe uma disciplina com este ID.")
    except ValueError:
        print("\n Erro: Valores de notas devem ser do tipo REAL.")

def selectDisciplina():
    declaracao = "SELECT id, nome, nota1, nota2 FROM disciplina_aluno ORDER BY nome"
    cur = conn.cursor() 
    cur.execute(declaracao)
    return cur.fetchall() 

def updateDisciplina(disId, nome, nota1, nota2):
    try:
        cur = conn.cursor() 
        declaracao = "UPDATE disciplina_aluno SET nome = ?, nota1 = ?, nota2 = ? WHERE id = ?"
        cur.execute(declaracao,(nome, nota1, nota2, disId))
        print("Entrou aqui")
        conn.commit()
    except ValueError:
        print("\n Erro: O ID deve ser INTEGER e as notas devem ser REAL.")

def deleteDisciplina(disId):
    try:
        declaracao = "DELETE FROM disciplina_aluno WHERE id = ?"
        cur = conn.cursor() 
        cur.execute(declaracao,(disId,))
        conn.commit()
    except ValueError:
        print("\n Erro: O ID deve ser um número.")

def clearDisciplina():
        declaracao = "DELETE FROM disciplina_aluno"
        cur = conn.cursor()
        cur.execute(declaracao)
        conn.commit()

