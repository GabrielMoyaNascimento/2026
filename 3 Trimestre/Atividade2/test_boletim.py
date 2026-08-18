import pytest
from boletim import validar_nota

# Testando o cenário feliz
def test_nota_valida_dentro_do_limite():
    assert validar_nota(7.5) is True
    assert validar_nota(0) is True
    assert validar_nota(10) is True

# Testando o cenário de erro (ValueError)
def test_nota_fora_do_limite_lanca_erro():
    with pytest.raises(ValueError) as erro:
        validar_nota(11)
    assert "entre 0 e 10" in str(erro.value)

# Testando outro cenário de erro (TypeError)
def test_nota_em_texto_lanca_erro_de_tipo():
    with pytest.raises(TypeError):
        validar_nota("dez")