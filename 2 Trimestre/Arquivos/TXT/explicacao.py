# Isso cria o arquivo vazio se ele não existir
# Se já existir, ele "limpa" o arquivo para começar do zero
open('arquivo.txt', 'w').close()

print("Arquivo pré-criado e pronto para uso!")


# Read - Modo de Leitura
with open('arquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
# Aqui o arquivo já foi fechado automaticamente pelo Python!

# Write - Modo de Escrita - Tomar cuidado
with open('lista.txt', 'w') as arquivo:
    arquivo.write('Maria')

# Append - Adiciona ao final da Lista 
with open('historico.txt', 'a') as arquivo:
    arquivo.write('\nVenda 2')
    arquivo.write('\nVenda 3')








usuario_nome = input("Digite seu nome: ")

# O modo 'w' abre o arquivo (e apaga o que tinha antes)
with open('usuario.txt', 'w') as arquivo:
    arquivo.write(usuario_nome) 

print("Nome salvo com sucesso!")


# Criando uma lista de presença dinâmica
while True:
    aluno = input("Digite o nome do aluno (ou 'fim' para parar): ")
    
    if aluno.lower() == 'fim':
        break
        
    with open('presenca.txt', 'a') as arquivo:
        # IMPORTANTE: Concatenamos(Unir) o input com '\n' para pular linha
        arquivo.write(aluno + '\n')

print("Lista de presença atualizada!")



busca = input("Qual arquivo você deseja consultar? ")

with open(busca, 'r') as arquivo:
    conteúdo = arquivo.read()
    print(f"\n--- Lendo {busca} ---\n{conteúdo}")
