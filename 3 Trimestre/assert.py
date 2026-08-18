
# Como funciona o assert?

# assert <condição_lógica>, "<mensagem_de_erro_opcional>"

def somar_valores(a, b):
    return a + b

# O Teste manual automatizado
assert somar_valores(2, 3) == 7, "Deveria ser 5"
# Se mudar para algo incorreto, o Python joga um AssertionError


def calcular_total_carrinho(itens):
    # GARANTA que o usuário mandou uma lista, senão pare tudo!
    assert type(itens) == list, "O carrinho precisa ser uma lista de preços."
    return sum(itens)

# --- ZONA DE TESTES ---

# Cenário 1: Sucesso (Ocorre em silêncio)
calcular_total_carrinho([10.5, 20.0, 5.0]) 

# Cenário 2: Falha (Vai jogar AssertionError: O carrinho precisa ser uma lista...)
calcular_total_carrinho("10.5, 20.0, 5.0")

def remover_vida(vida_atual, dano):
    nova_vida = vida_atual - dano
    
    # GARANTA que a vida não caiu abaixo de zero após o cálculo
    assert nova_vida >= 0, f"Erro crítico: Vida ficou negativa ({nova_vida})!"
    
    return nova_vida

# --- ZONA DE TESTES ---

# Cenário 1: Sucesso (Passa reto)
print(remover_vida(100, 40)) # Retorna 60

# Cenário 2: Falha (Dispara o erro na hora!)
print(remover_vida(20, 50))  # Crash: AssertionError: Erro crítico: Vida ficou negativa (-30)!


def criar_senha(senha_nova):
    # GARANTA que a senha tem o tamanho mínimo
    assert len(senha_nova) >= 8, "Segurança Fraca: A senha deve ter no mínimo 8 caracteres."
    return "Senha cadastrada com sucesso!"

# --- ZONA DE TESTES ---

# Cenário 1: Sucesso
print(criar_senha("python123"))

# Cenário 2: Falha
print(criar_senha("123")) # Crash imediato com a mensagem de erro