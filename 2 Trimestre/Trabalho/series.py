import sqlite3

BANCO_DADOS = 'sistema_escolar_completo.db'

def cadastrar_serie():
    print("\n--- Cadastrar Série ---")
    nome_serie = input("Nome da Série: ")
    try:
        id_escola = int(input("ID da Escola vinculada: "))
        
        conexao = sqlite3.connect(BANCO_DADOS)
        cursor = conexao.cursor()
        
        cursor.execute(f"INSERT INTO series (nome_serie, id_escola) VALUES ({nome_serie}, {id_escola})")
        conexao.commit()
        print("Série cadastrada e vinculada com sucesso!")
    except ValueError:
        print("Erro de Digitação: O ID da Escola precisa ser um número inteiro!")
    except sqlite3.IntegrityError:
        print("Erro de Vínculo: O ID da Escola informado NÃO existe!")
    finally:
        conexao.close()