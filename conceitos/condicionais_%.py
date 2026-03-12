id_usuario = int(input("Digite o ID do usuário: "))
valor_compra = float(input("Digite o valor da compra: R$ "))

# Regra: ID par AND valor > 500
if id_usuario % 2 == 0 and valor_compra > 500:
    print(f"Parabéns, usuário {id_usuario}! Você ganhou um cupom para sua compra de R$ {valor_compra}.")
else:
    print(f"Obrigado pela compra, usuário {id_usuario}. Continue acompanhando nossas promoções!")



ano = int(input("Digite o ano para verificar: "))

# Regra: (Divisível por 4 E não por 100) OU (Divisível por 400)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} é um ano comum.")



id_func = int(input("Digite o ID funcional: "))
temp = float(input("Temperatura da máquina (°C): "))
horas = float(input("Tempo de uso (horas): "))

# Regra: ID múltiplo de 3 AND (Temperatura > 40 OU Horas > 8)
if (id_func % 3 == 0) and (temp > 40 or horas > 8):
    print(f"Funcionário {id_func}, você foi escalado para a manutenção preventiva hoje. 🛠️")
else:
    print(f"Funcionário {id_func}, sua máquina opera dentro dos padrões normais.")



senha = input("Digite a senha: ")
tentativa = int(input("Número da tentativa atual: "))
token = input("Possui Token VIP? (s/n): ").lower()

# Regra: Senha correta AND (Tentativa múltipla de 3 OU Token VIP)
if senha == "admin123" and (tentativa % 3 == 0 or token == "s"):
    print(f"Tentativa nº {tentativa}: ACESSO CONCEDIDO. Bem-vindo!")
else:
    print(f"Tentativa nº {tentativa}: ACESSO BLOQUEADO POR PROTOCOLO.")




codigo = int(input("Digite o código do pacote: "))
peso = float(input("Digite o peso do pacote (kg): "))

if peso > 50:
    status = "CARGA PESADA"
elif peso < 5 and codigo % 10 == 0:
    status = "ENTREGA EXPRESSA"
else:
    status = "ENTREGA PADRÃO"

print(f"O pacote {codigo} com {peso}kg foi classificado como: {status}.")