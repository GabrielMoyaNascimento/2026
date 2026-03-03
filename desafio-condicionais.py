cliente = input("Nome do Cliente: ")
valor_original = float(input("Valor da Compra: R$ "))
distancia = int(input("Distância (km): "))
tem_cupom = input("Possui cupom? (S/N): ")

desconto = 0.0

if valor_original >= 1000.0 and tem_cupom == "S":
    desconto = valor_original * 0.20
elif valor_original > 500.0 and tem_cupom == "S":
    desconto = valor_original * 0.10

valor_com_desconto = valor_original - desconto

frete = 40.0
if distancia <= 50 and valor_com_desconto > 200.0:
    frete = 0.0

total_final = valor_com_desconto + frete

print("-" * 30)
print("RELATÓRIO DE COMPRA - ", cliente)
print("Valor Original: R$ ", valor_original)
print("Desconto: R$ ", desconto)
print("Frete: R$ ", frete)
print("TOTAL A PAGAR: R$ ", total_final)

if desconto == (valor_original * 0.20):
    print("SURPRESA: Você ganhou um Mousepad Gamer de brinde!")
print("-" * 30)