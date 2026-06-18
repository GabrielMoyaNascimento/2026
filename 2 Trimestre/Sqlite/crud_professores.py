import sqlite3


BANCO_DADOS = 'escola_demonstracao.db'

def cadastrar():
    print("\n--- Novo Cadastro ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    materia = input("Materia: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    salario = float(input("Salário: "))
    escola = input("Escola: ")

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    comando = f'''
        INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, escola)
        VALUES ('{nome}', '{telefone}', '{materia}', {idade}, '{cpf}', {salario}, '{escola}')
    '''
    cursor.execute(comando)
    conexao.commit()
    print("Professor cadastrado com sucesso!")
    conexao.close()  

def listar():
    print("\n--- Lista de professores ---")
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    # Read usando SELECT
    cursor.execute("SELECT * FROM professores")
    todos_professores = cursor.fetchall()

    if not todos_professores:
        print("Nenhum Professor cadastrado.")
    else:
        for p in todos_professores:
            print(f"ID: {p[0]} | Nome: {p[1]} | Matéria: {p[3]} | CPF: {p[5]}")

    conexao.close()

def atualizar():
    print("\n--- Atualizar Dados ---")
    id_busca = int(input("Digite o ID do Professor que deseja editar: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    # Primeiro, verificamos se o ID existe
    cursor.execute(f"SELECT * FROM professores WHERE id = {id_busca}")
    professor = cursor.fetchone() # Busca apenas uma linha

    if not professor:
        print("Professor não encontrado.")
        conexao.close()
        return

    print(f"Editando dados de: {professor[1]}")
    novo_nome = input(f"Novo Nome ({professor[1]}): ")
    novo_tel = input(f"Novo Telefone ({professor[2]}): ")
    nova_materia = input(f"Nova Matéria ({professor[3]}): ")
    nova_idade = int(input(f"Nova Idade ({professor[4]}): "))
    novo_cpf = input(f"Novo CPF ({professor[5]}): ")
    novo_salario = float(input(f"Novo Salário ({professor[6]}): "))
    nova_escola = input(f"Nova Escola ({professor[7]}): ")

    comando = f'''
        UPDATE professores 
        SET nome = '{novo_nome}', telefone = '{novo_tel}', turma = '{nova_materia}', 
                    idade = {nova_idade}, cpf = '{novo_cpf}',
                    salario = {novo_salario}, escola = '{nova_escola}'
        WHERE id = {id_busca}
    '''

    cursor.execute(comando)
    conexao.commit()
    conexao.close()
    print("Dados atualizados com sucesso!")

def excluir():
    print("\n--- Excluir Professor ---")
    id_busca = int(input("Digite o ID do Professor que deseja remover: "))

    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()

    # Delete usando o comando DELETE FROM do SQL baseado no ID
    comando = f"DELETE FROM professores WHERE id = {id_busca}"
    
    cursor.execute(comando)
    conexao.commit()

    conexao.close()

# --- MENU PRINCIPAL ---
def menu():
    conexao = sqlite3.connect(BANCO_DADOS)
    cursor = conexao.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            materia TEXT,
            idade INTEGER,
            cpf TEXT UNIQUE NOT NULL,
            salario REAL,
            escola TEXT
        )
    ''')

    conexao.commit()
    conexao.close()

    while True:
        print("\n=== SISTEMA ESCOLAR (SQLITE) ===")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Atualizar Professor")
        print("4. Excluir Professor")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()