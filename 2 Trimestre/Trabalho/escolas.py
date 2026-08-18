import sqlite3

BANCO_DADOS = 'sistema_escolar_completo.db'

def cadastrar_escola():
    print("\n--- Cadastrar Escola ---")
    nome = input("Nome da Escola: ")
    endereco = input("Endereço: ")
    
    try:
        conexao = sqlite3.connect(BANCO_DADOS)
        cursor = conexao.cursor()
        cursor.execute(f"INSERT INTO escolas (nome, endereco) VALUES ({nome}, {endereco})")
        conexao.commit()
        print("Escola cadastrada com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")
    finally:
        conexao.close()