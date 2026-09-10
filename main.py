import entrada
import apresentacao
import calculos


def main():
    matriz = None

    while True:
        print()
        print("=" * 45)
        print("SISTEMA DE ÁLGEBRA LINEAR")
        print("=" * 45)
        print("1 - Criar matriz")
        print("2 - Exibir matriz")
        print("3 - Calcular determinante")
        print("4 - Verificar se possui inversa")
        print("5 - Calcular inversa")
        print("6 - Calcular transposta")
        print("7 - Multiplicar matrizes")
        print("0 - Sair")
        print("=" * 45)

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            matriz = entrada.ler_matriz()
            print("\nMatriz criada com sucesso.")
            apresentacao.mostrar_matriz(matriz, "A")

        elif opcao == "2":
            if matriz is None:
                print("\nNenhuma matriz foi criada.")
            else:
                apresentacao.mostrar_matriz(matriz, "A")

        elif opcao == "3":
            if matriz is None:
                print("\nNenhuma matriz foi criada.")
            else:
                try:
                    det = calculos.determinante(matriz)
                    print(f"\ndet(A) = {det:.4f}")
                except ValueError as erro:
                    print(f"\nErro: {erro}")

        elif opcao == "4":
            if matriz is None:
                print("\nNenhuma matriz foi criada.")
            else:
                if len(matriz) != len(matriz[0]):
                    print("\nA matriz precisa ser quadrada.")
                elif calculos.possui_inversa(matriz):
                    print("\nA matriz possui inversa.")
                else:
                    print("\nA matriz não possui inversa.")

        elif opcao == "5":
            if matriz is None:
                print("\nNenhuma matriz foi criada.")
            else:
                try:
                    inversa = calculos.inversa(matriz)
                    apresentacao.mostrar_matriz(inversa.tolist(), "A⁻¹")
                except Exception as erro:
                    print(f"\nErro: {erro}")

        elif opcao == "6":
            if matriz is None:
                print("\nNenhuma matriz foi criada.")
            else:
                transposta = calculos.transposta(matriz)
                apresentacao.mostrar_matriz(transposta.tolist(), "Aᵀ")

        elif opcao == "7":
            if matriz is None:
                print("\nCrie a matriz A primeiro.")
            else:
                print("\nAgora vamos criar a matriz B.")
                matriz_b = entrada.ler_matriz()

                try:
                    resultado = calculos.multiplicar(matriz, matriz_b)
                    apresentacao.mostrar_matriz(resultado.tolist(), "A × B")
                except ValueError as erro:
                    print(f"\nErro: {erro}")

        elif opcao == "0":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    main()