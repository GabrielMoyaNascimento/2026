# Slicing
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del num[3:7] # Remove 3, 4, 5, 6 (para antes do índice 7)
print(f"Num: {num}, Tamanho: {len(num)}")

# Transferência
pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"]
concluidos = []
item = pendentes.pop(0)
concluidos.append(item)
print(f"Pendentes: {pendentes}\nConcluídos: {concluidos}")

# Calculadora
n = [10, 20, 5, 0]
n[3] = n[0] + n[1]
print(f"Lista atualizada: {n}")

# Localizador
cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
busca = input("Cidade: ")
if busca in cidades:
    print(f"Posição: {cidades.index(busca)}")
else:
    print("Não encontrada.")

# Limpeza
usuarios = ["admin", "convidado", "suporte", "teste"]
usuarios.remove("teste")
del usuarios[0]
print(f"Resultado: {usuarios}")


# Desafio
disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
emprestados = []

# Simulação de Empréstimo
pedido = input("Livro para empréstimo: ")
if pedido in disponiveis:
    disponiveis.remove(pedido)
    emprestados.append(pedido)
    print("✅ Empréstimo realizado!")
else:
    print("❌ Livro indisponível.")

# Simulação de Devolução
devolucao = input("Livro para devolver: ")
if devolucao in emprestados:
    emprestados.remove(devolucao)
    disponiveis.append(devolucao)
    print("✅ Devolução aceita!")
else:
    print("⚠️ Este livro não é nosso ou não foi emprestado.")

# Manutenção (Deletar os 2 primeiros velhos)
if len(disponiveis) >= 2:
    del disponiveis[0:2]

print(f"\nAcervo Atual: {disponiveis}")
print(f"Emprestados Agora: {emprestados}")