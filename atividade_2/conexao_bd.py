import sqlite3

arq_db = "gerenciador_disciplina.db"

def conecta_bd():
    conn = sqlite3.connect(arq_db)
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS disciplina_aluno (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        nota1 REAL,
        nota2 REAL
    );
    """)
    conn.commit()
    return conn