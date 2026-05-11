estoque = []


def adicionar_produto(nome):
    if nome.strip(): # Valida se não está vazio
        estoque.append(nome)
        print(f"✅ Produto '{nome}' adicionado!")
    else:
        print("❌ Erro: O nome do produto não pode ser vazio.")

def listar_produtos():
    print("\n" + "="*20)
    print("   ITENS EM ESTOQUE")
    print("="*20)
    if not estoque:
        print("O estoque está vazio.")
    else:
        for i, produto in enumerate(estoque):
            print(f"[{i}] - {produto}")
    print("="*20)

def atualizar_produto(indice, novo_nome):
    try:
        estoque[indice] = novo_nome
        print("🔄 Produto atualizado com sucesso!")
    except IndexError:
        print("❌ Erro: Índice não encontrado.")

def remover_produto(indice):
    try:
        removido = estoque.pop(indice)
        print(f"🗑️ Produto '{removido}' removido.")
    except IndexError:
        print("❌ Erro: Não foi possível remover. Índice inválido.")


def exibir_menu():
    while True:
        listar_produtos()
        print("\nSISTEMA DE GESTÃO")
        print("1. Adicionar Produto")
        print("2. Atualizar Produto")
        print("3. Remover Produto")
        print("0. Sair")
        
        opcao = input("\nEscolha uma operação: ")

        if opcao == "1":
            nome = input("Digite o nome do novo produto: ")
            adicionar_produto(nome)
        
        elif opcao == "2":
            idx = int(input("Digite o índice que deseja alterar: "))
            novo = input("Digite o novo nome: ")
            atualizar_produto(idx, novo)
            
        elif opcao == "3":
            idx = int(input("Digite o índice que deseja remover: "))
            remover_produto(idx)
            
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")


exibir_menu()