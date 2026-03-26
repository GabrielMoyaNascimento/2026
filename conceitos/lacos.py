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

# 4. Fila
fila = ["A", "B", "C", "D", "E"]
while len(fila) > 0:
    atendido = fila.pop(0)
    print(f"Atendido: {atendido}")

# 5. Compras
carrinho = []
item = ""
while item != "fim":
    item = input("Produto: ")
    if item != "fim":
        carrinho.append(item)
for produto in carrinho:
    print(produto)