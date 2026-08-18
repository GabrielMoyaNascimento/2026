import sqlite3
# Importa o inicializador de tabelas do banco
from banco import inicializar_banco, BANCO_DADOS

# Importa as funções específicas criadas em cada arquivo-módulo separado
from escolas import cadastrar_escola
from professores import cadastrar_professor
from series import cadastrar_serie
from turmas import cadastrar_turma
from alunos import cadastrar_aluno

def listar_tudo():
    print("\n=============================================")
    print("         RELATÓRIO GERAL DO SISTEMA          ")
    print("=============================================")
    try:
        conexao = sqlite3.connect(BANCO_DADOS)
        cursor = conexao.cursor()
        
        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        print("\nESCOLAS:")
        for e in escolas : print(f"ID: {e[0]} | Nome: {e[1]} | Endereço: {e[2]}")
            
        cursor.execute("SELECT * FROM professores")
        professores = cursor.fetchall()

        print("\nPROFESSORES:")
        for p in professores: print(f"ID: {p[0]} | Nome: {p[1]} | Matéria: {p[2]} | CPF: {p[3]}")
            
        cursor.execute("SELECT * FROM series")
        series = cursor.fetchall()

        print("\nSÉRIES:")
        for s in series: print(f"ID: {s[0]} | Série: {s[1]} | ID Escola Pai: {s[2]}")
            
        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        print("\nTURMAS:")
        for t in turmas: print(f"ID: {t[0]} | Turma: {t[1]} | ID Série: {t[2]} | ID Prof: {t[3]}")
            
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        print("\nALUNOS MATRICULADOS:")
        for a in alunos: print(f"ID: {a[0]} | Nome: {a[1]} | CPF: {a[2]} | ID Turma: {a[3]}")
            
    except sqlite3.Error as e:
        print(f"Erro ao gerar relatório: {e}")
    finally:
        conexao.close()
    print("=============================================\n")

def menu():
    # Executa a conferência das tabelas assim que o programa inicia
    inicializar_banco()
    
    while True:
        print("=== SISTEMA ESCOLAR MODULAR ===")
        print("1. Cadastrar Escola")
        print("2. Cadastrar Professor")
        print("3. Cadastrar Série")
        print("4. Cadastrar Turma")
        print("5. Cadastrar Aluno")
        print("6. Relatório Geral (Listar Tudo)")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar_escola()
        elif opcao == '2': cadastrar_professor()
        elif opcao == '3': cadastrar_serie()
        elif opcao == '4': cadastrar_turma()
        elif opcao == '5': cadastrar_aluno()
        elif opcao == '6': listar_tudo()
        elif opcao == '7': 
            print("Encerrando o ecossistema do sistema escolar. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()