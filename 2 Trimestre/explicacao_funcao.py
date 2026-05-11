def calcular_valor_total(valor1, valor2, valor3):
    total = valor1+valor2+valor3
    return total # devolvendo o valor

valor1 = float(input("Digite o valor 1: "))
valor2 = float(input("Digite o valor 2: "))
valor3 = float(input("Digite o valor 3: "))

valor_total = calcular_valor_total(valor1,valor2,valor3)
print("Valor total é: ", valor_total)
