# 1. Entrada VIP no Show

idade = int(input("Digite sua idade: "))
ingresso_vip = input("Você possui ingresso VIP? (s/n): ")
na_lista = input("Você está na lista de convidados? (s/n): ")

# A idade é obrigatória, mas basta UM dos outros dois requisitos
if idade > 18 and (ingresso_vip == "s" or na_lista == "s"):
    print("Seja bem vindo!")
else:
    print("Acesso negado.")

#2. Seleção de Bolsa de Estudos
media = float(input("Digite sua média escolar: "))
renda = float(input("Digite sua renda familiar: "))
escola_publica = input("Veio de escola pública? (s/n): ")

# Média alta é obrigatória; renda baixa OU origem pública são os diferenciais
if media > 8.0 and (renda < 2000.0 or escola_publica == "s"):
    print("Ganhou a bolsa")
else:
    print("Não atende aos requisitos")


#3. Sistema de Autenticação "Admin"
usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

# Aceita qualquer um dos dois usuários, desde que a senha esteja correta
if (usuario == "admin" or usuario == "root") and senha == "12345":
    print("Acesso liberado")
else:
    print("Usuário ou senha incorretos.")


#4. Promoção de E-commerce
valor_compra = float(input("Digite o valor total da compra: R$ "))
eh_prime = input("Você é assinante Prime? (s/n): ")

# Lógica para frete grátis
if valor_compra > 500.0 or (eh_prime == "s" and valor_compra > 100.0):
    frete = 0.0
    print("Parabéns! Você ganhou frete grátis.")
else:
    frete = 50.0
    print("O valor do frete para esta compra é R$ 50,00.")

valor_total = valor_compra + frete

print(f"Valor total a pagar: R$ {valor_total:.2f}")

#Desafio

print("=== SISTEMA DE CONTROLE DO REATOR ===")

cargo = input("Qual o seu cargo? ").upper() # .upper() ajuda a evitar erros de digitação
codigo = int(input("Código de Acesso: "))
emergencia = input("Botão de emergência ativado? (s/n): ")
epi = input("Está usando todos os EPIs? (s/n): ")

# A lógica "Mestra"
if (cargo == "ENGENHEIRO" or cargo == "TECNICO") and (codigo == 1234 or emergencia == "s") and epi == "s":
    print("\n[OK] ACESSO LIBERADO. Trabalhe com cuidado!")
else:
    print("\n[ERRO] ACESSO NEGADO: REQUISITOS NÃO ATENDIDOS.")