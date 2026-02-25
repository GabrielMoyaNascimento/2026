# 1. Montanha-Russa
nome = input("Nome do cliente: ")
altura = float(input("Altura em metros: "))

if altura < 1.50:
    print("Desculpe, você não tem a altura mínima ", nome)
else:
    print("Acesso liberado! Divirta-se na queda livre, ", nome)

# 2. Battle System
ataque = int(input("Poder de ataque do herói: "))
defesa = int(input("Defesa do vilão: "))
dano = ataque - defesa

if dano <= 0:
    print("O vilão bloqueou o ataque! Dano: 0")
else:
    print("Ataque crítico! Você causou dano ao vilão de", dano)

# 3. Cupom DEV10
total = float(input("Valor da compra: R$ "))
cupom = input("Digite o cupom: ")

if cupom == "DEV10":
    desconto = total * 0.10
    novo_total = total - desconto
    print("Cupom aceito! Novo total: R$ ", novo_total)
else:
    print("Cupom inválido. Valor original: R$ ", total)

# 4. Sensor Data Center
temp = float(input("Temperatura do servidor: "))

if temp >= 80:
    print("PERIGO! Desligando servidor!")
elif temp >= 50:
    print("Alerta: Ventoinhas no máximo!")
else:
    print("Temperatura estável.")