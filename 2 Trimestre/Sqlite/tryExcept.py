import sqlite3

BANCO_TESTE = "banco_testes_erros.db"

# ---------------------------------------------------------------------
# 1. Testando ValueError e ZeroDivisionError
# ---------------------------------------------------------------------
def calcular_divisao_professores():
    print("\n--- Teste 1: ValueError ou ZeroDivisionError ---")
    try:
        # Para testar ValueError: Digite uma letra (ex: 'cinco')
        # Para testar ZeroDivisionError: Digite o número 0
        total_professores = int(input("Digite o total de professores: "))
        turmas = int(input("Digite o número de turmas para dividir: "))
        
        resultado = total_professores / turmas
        print(f"Média: {resultado} professores por turma.")
        
    except ValueError:
        print("Capturado: ValueError! Você tentou converter texto em número.")
    except ZeroDivisionError:
        print("Capturado: ZeroDivisionError! Não existe divisão por zero na matemática.")

# ---------------------------------------------------------------------
# 2. Testando IndexError
# ---------------------------------------------------------------------
def buscar_professor_na_lista():
    print("\n--- Teste 2: IndexError ---")
    lista_profs = ["Allan", "Marcos", "Julia"] # Índices: 0, 1 e 2
    
    try:
        # Para testar IndexError: Digite o número 5 ou qualquer um fora de 0 a 2
        indice = int(input("Digite o índice do professor que quer ver (0 a 2): "))
        print(f"O professor escolhido foi: {lista_profs[indice]}")
        
    except IndexError:
        print("Capturado: IndexError! Você buscou uma posição que não existe na lista.")
    except ValueError:
        print("Capturado: ValueError! Digite um número inteiro no índice.")

# ---------------------------------------------------------------------
# 3. Testando sqlite3.OperationalError
# ---------------------------------------------------------------------
def erro_de_digitacao_sql():
    print("\n--- Teste 3: sqlite3.OperationalError ---")
    conexao = sqlite3.connect(BANCO_TESTE)
    cursor = conexao.cursor()
    
    try:
        # Forçando o erro: A tabela 'professores_fantasmas' NÃO existe no banco
        cursor.execute("SELECT * FROM professores_fantasmas;")
        cursor.fetchall()
        
    except sqlite3.OperationalError as erro:
        print(f"Capturado: sqlite3.OperationalError!")
        print(f"Mensagem real do banco: {erro}")
        
    finally:
        conexao.close()

# ---------------------------------------------------------------------
# 4. Testando sqlite3.IntegrityError
# ---------------------------------------------------------------------
def criar_ambiente_e_testar_integridade():
    print("\n--- Teste 4: sqlite3.IntegrityError ---")
    conexao = sqlite3.connect(BANCO_TESTE)
    cursor = conexao.cursor()
    
    # Criando tabela com CPF único para o teste
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS teste_prof (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT UNIQUE
        )
    ''')
    conexao.commit()
    
    # Inserindo o primeiro CPF
    cursor.execute("INSERT INTO teste_prof (nome, cpf) VALUES ('Professor A', '111.111.111-11');")
    conexao.commit()

    try:
        print("Tentando inserir outro professor com o MESMO CPF...")
        # Forçando o erro: Inserir o mesmo CPF que já existe na tabela
        cursor.execute("INSERT INTO teste_prof (nome, cpf) VALUES ('Professor B', '111.111.111-11');")
        conexao.commit()
        
    except sqlite3.IntegrityError as erro:
        print(f"Mensagem real do banco: {erro} (O campo CPF é UNIQUE!)")
        
    finally:
        # Limpa a tabela para o próximo teste e fecha
        cursor.execute("DROP TABLE teste_prof;")
        conexao.commit()
        conexao.close()

calcular_divisao_professores()
buscar_professor_na_lista()
erro_de_digitacao_sql()
criar_ambiente_e_testar_integridade()