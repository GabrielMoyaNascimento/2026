def validar_nota(nota):
    if not isinstance(nota, (int, float)):
        raise TypeError("A nota deve ser um número.")
    if nota < 0 or nota > 10:
        raise ValueError("A nota deve estar entre 0 e 10.")
    return True