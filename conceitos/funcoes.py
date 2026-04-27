# 1
def avaliar_desempenho(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota >= 5:
        return "Regular"
    else:
        return "Insuficiente"

n = float(input("Digite a nota do aluno (0-10): "))
resultado = avaliar_desempenho(n)
print(f"O desempenho foi: {resultado}")

# 2
def senha_valida(senha):
    if len(senha) >= 6:
        return True
    else:
        return False

print("--- Cadastro de Senha ---")
while True:
    s = input("Crie uma senha (min. 6 caracteres): ")
    if senha_valida(s):
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Erro: Senha muito curta. Tente novamente.")

# 3
def aplicar_promocao(lista_precos):
    nova_lista = []
    for preco in lista_precos:
        if preco > 100:
            desconto = preco * 0.85 # 15% de desconto
            nova_lista.append(desconto)
        else:
            nova_lista.append(preco)
    return nova_lista


compras = [150.0, 80.0, 200.0, 50.0]
precos_finais = aplicar_promocao(compras)

print(f"Preços originais: {compras}")
print(f"Preços com promoção: {precos_finais}")


# 4
def esta_na_lista(lista, busca):
    for item in lista:
        if item.lower() == busca.lower():
            return "Encontrado!"
    return "Não disponível"


frutas = ["Maçã", "Banana", "Uva", "Manga"]
item_procurado = input("O que deseja buscar no estoque? ")

status = esta_na_lista(frutas, item_procurado)
print(f"Status: {status}")


# 5
def sofrer_dano(vida_atual, valor_dano):
    nova_vida = vida_atual - valor_dano
    return nova_vida

vida_heroi = 100

print(f"--- Início da Batalha! Vida: {vida_heroi} ---")

while vida_heroi > 0:
    dano = int(input("Quanto de dano o monstro causou? "))
    vida_heroi = sofrer_dano(vida_heroi, dano)
    
    if vida_heroi > 0:
        print(f"O herói ainda resiste! Vida restante: {vida_heroi}")
    else:
        print("O herói caiu em batalha... Game Over.")


# ------------------------------------------------------------------------------

# 1. Conversor
def converter_km_para_ms(velocidade):
    return velocidade / 3.6

v = float(input("Velocidade (km/h): "))
if v > 80:
    print(f"{v} km/h equivale a {converter_km_para_ms(v):.2f} m/s. Reduza!")

# 2. Área
def calcular_area(larg, comp):
    return larg * comp

for i in range(1, 4):
    l = float(input(f"Largura do terreno {i}: "))
    c = float(input(f"Comprimento do terreno {i}: "))
    print(f"Área: {calcular_area(l, c)}m²")

# 3. Contador
def contar_caracteres(texto):
    return len(texto)

usuario = input("Digite seu user: ")
if contar_caracteres(usuario) < 5:
    print("Nome de usuário muito curto.")
else:
    print("Nome aceito.")

# 4. Carrinho
def somar_carrinho(lista):
    total = sum(lista)
    if total > 500:
        total *= 0.90
    return total

precos = [200, 150, 300]
print(f"Total a pagar: R$ {somar_carrinho(precos)}")

# 5. Paridade
def eh_par(num):
    return num % 2 == 0

n = int(input("Número: "))
if eh_par(n):
    print("Este número é par.")
else:
    print("Este número é ímpar.")