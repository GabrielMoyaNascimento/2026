# 1. Inspetor de Qualidade
comp = input("Comprimento OK? (s/n): ")
if comp == "s":
    larg = input("Largura OK? (s/n): ")
    if larg == "s":
        print("PEÇA APROVADA")
    else:
        print("REPROVADO: Problema na largura")
else:
    print("REPROVADO: Problema no comprimento")


# 2. Segurança na Fábrica
curso = input("Concluiu o curso? (s/n): ")
if curso == "s":
    instrutor = input("Instrutor presente? (s/n): ")
    if instrutor == "s":
        print("Acesso Liberado: Operação iniciada")
    else:
        print("Aguarde o instrutor para ligar a máquina")
else:
    print("Acesso Negado: Faça o treinamento primeiro")


# 3. Monitor de Estufa
temp = float(input("Temperatura: "))
if temp > 30:
    print("Alerta de Calor!")
    umid = float(input("Umidade: "))
    if umid < 40:
        print("Ação: Ligar Irrigação!")
    else:
        print("Ação: Ligar apenas ventiladores")
else:
    print("Clima estável")


# Desafio
print("=== SISTEMA DE CONTROLE DE POUSO - DRONE CARGO ===")

codigo = int(input("Código do Drone: "))
autorizacao = input("Autorização da torre (s/n): ")

if codigo == 999 or autorizacao == "s":
    print("\n--- Identificação Concluída. Analisando sensores... ---")

    bateria = float(input("Nível da Bateria (%): "))
    clima = input("Clima (ensolarado/chuvoso): ").lower()
    vento = float(input("Velocidade do Vento (km/h): "))

    if bateria < 10:
        print("\n[ALERTA] BATERIA CRÍTICA! POUSO DE EMERGÊNCIA AUTORIZADO.")
    
    elif (clima == "ensolarado" and vento < 30) or (clima == "chuvoso" and vento < 10):
        print("\n[OK] POUSO AUTORIZADO: Iniciando descida.")
    
    else:
        print("\n[AVISO] POUSO NEGADO: Condições meteorológicas perigosas.")

else:
    print("\n[ERRO] 01: Drone não identificado. Retornando à base.")