def converter_id(valor_input):
    try:
        return int(valor_input)
    except ValueError:
        raise ValueError("O ID inserido deve ser estritamente numérico.")