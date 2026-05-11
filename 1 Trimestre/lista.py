# 1. Seleção
filmes = ["Matrix", "Inception", "Avatar", "Gladiador", "Up"]
print(f"Primeiro: {filmes[0]}, Último: {filmes[4]}")

# 2. Atualização
estoque = ["Teclado", "Mouse", "Monitor"]
estoque[2] = "Webcam"
print(f"Estoque atualizado: {estoque}")

# 3. Ficha
cliente = ["Marcos", 25, 1.80, True]
print(f"O cliente {cliente[0]} tem {cliente[1]} anos e sua altura é {cliente[2]}m.")

# 4. len()
vendas = [150.50, 200.00, 50.00, 300.20, 120.00, 450.00]
total = len(vendas)
print(f"Hoje foram realizadas {total} vendas.")

# 5. Cores
cores = ["Vermelho", "Verde", "Azul", "Amarelo", "Preto"]
escolha = int(input("Escolha de 1 a 5: "))
print(f"A cor escolhida foi: {cores[escolha]}")