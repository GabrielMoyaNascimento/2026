import pytest
from processador import converter_id

def test_conversao_com_sucesso():
    assert converter_id("15") == 15

def test_conversao_deve_lancar_erro_com_texto():
    with pytest.raises(ValueError) as erro:
        converter_id("Premium")
    
    assert "estritamente numérico" in str(erro.value)