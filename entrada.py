from validacoes import eh_numero, eh_inteiro_positivo


def ler_inteiro_positivo(mensagem):
    while True:
        valor = input(mensagem).strip()

        if eh_inteiro_positivo(valor):
            return int(valor)

        print("Digite um número inteiro maior que zero.")


def ler_matriz():
    linhas = ler_inteiro_positivo("Quantidade de linhas: ")
    colunas = ler_inteiro_positivo("Quantidade de colunas: ")

    matriz = []

    print(f"Digite os valores da matriz {linhas}x{colunas}:")

    for i in range(linhas):
        while True:
            valores = input(f"Linha {i + 1}: ").strip().split()

            if len(valores) != colunas:
                print(f"Digite exatamente {colunas} valores.")
                continue

            if not all(eh_numero(valor) for valor in valores):
                print("Digite apenas números.")
                continue

            linha = [float(valor) for valor in valores]
            matriz.append(linha)
            break

    return matriz