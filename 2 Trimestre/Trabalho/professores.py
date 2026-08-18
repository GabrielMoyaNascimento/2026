import sqlite3

BANCO_DADOS = 'sistema_escolar_completo.db'

def cadastrar_professor():
    print("\n--- Cadastrar Professor ---")
    nome = input("Nome do Professor: ")
    materia = input("Matéria: ")
    cpf = input("CPF: ")
    
    try:
        conexao = sqlite3.connect(BANCO_DADOS)
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO professores (nome, materia, cpf) VALUES ({nome}, {materia}, {cpf})")
        conexao.commit()
        print("Professor cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Este CPF já está cadastrado para outro professor!")
    finally:
        conexao.close()