import sqlite3

BANCO_DADOS = 'sistema_escolar_completo.db'

def cadastrar_aluno():
    print("\n--- Cadastrar Aluno ---")
    nome = input("Nome do Aluno: ")
    cpf = input("CPF do Aluno: ")
    try:
        id_turma = int(input("ID da Turma do Aluno: "))
        
        conexao = sqlite3.connect(BANCO_DADOS)
        cursor = conexao.cursor()
        
        cursor.execute(f"INSERT INTO alunos (nome, cpf, id_turma) VALUES ({nome}, {cpf}, {id_turma})")
        conexao.commit()
        print("Aluno matriculado com sucesso!")
    except ValueError:
        print("Erro de Digitação: O ID da Turma precisa ser um número inteiro!")
    except sqlite3.IntegrityError:
        print("Erro: CPF já cadastrado OU o ID da Turma informado não existe!")
    finally:
        conexao.close()