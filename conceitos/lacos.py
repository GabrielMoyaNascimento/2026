# 1. Soma
precos = [10, 20, 30, 40, 50]
total = 0
for p in precos:
    total += p
print(total)

# 2. Login
senha = ""
while senha != "1234":
    senha = input("Senha: ")
print("Bem vindo")

# 3. Tamanho do Nome
nomes = ["Gabriel", "João Guilherme", "Ayumi", "Isadora", "Ana"]
nomes_escolhidos = []

for nome in nomes:
    if len(nome) > 5:
        nomes_escolhidos.append(nome)
    print(nome)


# 4. Fila
fila = ["A", "B", "C", "D", "E"]
while len(fila) > 0:
    print(f"Atendido: {fila[0]}")
    fila.pop(0)
    

# 5. Compras
carrinho = []
item = ""
while item != "fim":
    item = input("Produto: ")
    if item != "fim":
        carrinho.append(item)
for produto in carrinho:
    print(produto)