import sqlite3

BANCO_DADOS = 'sistema_escolar_completo.db'

def cadastrar_turma():
    print("\n--- Cadastrar Turma ---")
    nome_turma = input("Nome da Turma: ")
    try:
        id_serie = int(input("ID da Série vinculada: "))
        id_professor = int(input("ID do Professor desta Turma: "))
        
        conexao = sqlite3.connect(BANCO_DADOS)
        cursor = conexao.cursor()
        
        cursor.execute(f"INSERT INTO turmas (nome_turma, id_serie, id_professor) VALUES ({nome_turma}, {id_serie}, {id_professor})")
        conexao.commit()
        print("Turma criada e vinculada!")
    except ValueError:
        print("Erro de Digitação: Os IDs precisam ser números inteiros!")
    except sqlite3.IntegrityError:
        print("Erro de Vínculo: O ID da Série ou o ID do Professor não existem!")
    finally:
        conexao.close()