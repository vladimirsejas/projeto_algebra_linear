def formatar_numero(valor):
    if valor.is_integer():
        return str(int(valor))
    return f"{valor:.4f}".rstrip("0").rstrip(".")


def mostrar_matriz(matriz, nome=""):
    if nome:
        print(f"\n{nome} =")

    for linha in matriz:
        valores = [formatar_numero(valor) for valor in linha]
        print("[ " + "  ".join(valores) + " ]")