import sqlite3

BANCO_DADOS = 'sistema_escolar_completo.db'

def inicializar_banco():
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            materia TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_serie TEXT NOT NULL,
            id_escola INTEGER,
            FOREIGN KEY (id_escola) REFERENCES escolas(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_turma TEXT NOT NULL,
            id_serie INTEGER,
            id_professor INTEGER,
            FOREIGN KEY (id_serie) REFERENCES series(id),
            FOREIGN KEY (id_professor) REFERENCES professores(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL,
            id_turma INTEGER,
            FOREIGN KEY (id_turma) REFERENCES turmas(id)
        )
    ''')
    conexao.commit()
    conexao.close()

inicializar_banco()