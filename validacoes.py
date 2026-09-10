def eh_numero(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def eh_inteiro_positivo(valor):
    try:
        return int(valor) > 0
    except ValueError:
        return False