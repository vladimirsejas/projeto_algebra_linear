import sys
from pathlib import Path
import tkinter as tk

sys.path.append(str(Path(__file__).resolve().parent.parent))

import calculos


def criar_campos_matriz(area, linhas, colunas):
    campos = []

    for i in range(linhas):
        linha = []

        for j in range(colunas):
            campo = tk.Entry(area, width=8, justify="center")
            campo.grid(row=i, column=j, padx=4, pady=4)
            linha.append(campo)

        campos.append(linha)

    return campos


def ler_campos(campos):
    if not campos:
        raise ValueError("Crie uma matriz primeiro.")

    matriz = []

    for linha in campos:
        valores = []

        for campo in linha:
            texto = campo.get().strip().replace(",", ".")

            if texto == "":
                raise ValueError("Preencha todos os campos.")

            try:
                valores.append(float(texto))
            except ValueError:
                raise ValueError("Digite apenas números.")

        matriz.append(valores)

    return matriz


def formatar_numero(valor):
    valor = float(valor)

    if abs(valor) < 1e-10:
        valor = 0.0

    if valor.is_integer():
        return str(int(valor))

    return f"{valor:.4f}".rstrip("0").rstrip(".")


def formatar_matriz(matriz):
    linhas = []

    for linha in matriz:
        valores = "   ".join(formatar_numero(valor) for valor in linha)
        linhas.append(f"[  {valores}  ]")

    return "\n".join(linhas)


def mostrar_resultado(titulo, conteudo):
    for widget in area_resultado.winfo_children():
        widget.destroy()

    tk.Label(
        area_resultado,
        text=titulo,
        font=("Arial", 14)
    ).pack(pady=5)

    tk.Label(
        area_resultado,
        text=conteudo,
        font=("Courier New", 13),
        justify="left"
    ).pack()


def criar_matriz_a():
    global campos_a

    try:
        linhas = int(campo_linhas_a.get())
        colunas = int(campo_colunas_a.get())

        if linhas <= 0 or colunas <= 0:
            raise ValueError

    except ValueError:
        mensagem.config(
            text="Linhas e colunas devem ser inteiros maiores que zero."
        )
        return

    for widget in area_a.winfo_children():
        widget.destroy()

    campos_a = criar_campos_matriz(area_a, linhas, colunas)

    mensagem.config(
        text=f"Matriz A {linhas}x{colunas} criada."
    )


def criar_matriz_b():
    global campos_b

    try:
        linhas = int(campo_linhas_b.get())
        colunas = int(campo_colunas_b.get())

        if linhas <= 0 or colunas <= 0:
            raise ValueError

    except ValueError:
        mensagem.config(
            text="Linhas e colunas de B devem ser inteiros maiores que zero."
        )
        return

    for widget in area_b.winfo_children():
        widget.destroy()

    campos_b = criar_campos_matriz(area_b, linhas, colunas)

    mensagem.config(
        text=f"Matriz B {linhas}x{colunas} criada."
    )


def obter_a():
    return ler_campos(campos_a)


def mostrar_a():
    try:
        matriz = obter_a()

        mostrar_resultado(
            "Matriz A",
            formatar_matriz(matriz)
        )

        mensagem.config(text="")

    except ValueError as erro:
        mensagem.config(text=str(erro))


def calcular_determinante():
    try:
        matriz = obter_a()

        if len(matriz) != len(matriz[0]):
            mensagem.config(text="A matriz precisa ser quadrada.")
            return

        det = calculos.determinante(matriz)

        mostrar_resultado(
            "Determinante",
            f"det(A) = {formatar_numero(det)}"
        )

        mensagem.config(text="")

    except ValueError as erro:
        mensagem.config(text=str(erro))


def verificar_inversa():
    try:
        matriz = obter_a()

        if len(matriz) != len(matriz[0]):
            mensagem.config(text="A matriz precisa ser quadrada.")
            return

        if calculos.possui_inversa(matriz):
            texto = "A matriz possui inversa."
        else:
            texto = "A matriz não possui inversa."

        mostrar_resultado(
            "Verificação",
            texto
        )

        mensagem.config(text="")

    except ValueError as erro:
        mensagem.config(text=str(erro))


def calcular_inversa():
    try:
        matriz = obter_a()

        if len(matriz) != len(matriz[0]):
            mensagem.config(text="A matriz precisa ser quadrada.")
            return

        if not calculos.possui_inversa(matriz):
            mensagem.config(text="A matriz não possui inversa.")
            return

        resultado = calculos.inversa(matriz)

        mostrar_resultado(
            "Matriz A⁻¹",
            formatar_matriz(resultado.tolist())
        )

        mensagem.config(text="")

    except ValueError as erro:
        mensagem.config(text=str(erro))


def calcular_transposta():
    try:
        matriz = obter_a()

        resultado = calculos.transposta(matriz)

        mostrar_resultado(
            "Matriz Aᵀ",
            formatar_matriz(resultado.tolist())
        )

        mensagem.config(text="")

    except ValueError as erro:
        mensagem.config(text=str(erro))


def calcular_multiplicacao():
    try:
        matriz_a = obter_a()
        matriz_b = ler_campos(campos_b)

        if len(matriz_a[0]) != len(matriz_b):
            mensagem.config(
                text="O número de colunas de A deve ser igual ao número de linhas de B."
            )
            return

        resultado = calculos.multiplicar(
            matriz_a,
            matriz_b
        )

        mostrar_resultado(
            "A × B",
            formatar_matriz(resultado.tolist())
        )

        mensagem.config(text="")

    except ValueError as erro:
        mensagem.config(text=str(erro))


janela = tk.Tk()

janela.title("Sistema de Álgebra Linear")
janela.geometry("900x750")
janela.minsize(800, 650)

campos_a = []
campos_b = []

titulo = tk.Label(
    janela,
    text="SISTEMA DE ÁLGEBRA LINEAR",
    font=("Arial", 20)
)

titulo.pack(pady=15)

subtitulo = tk.Label(
    janela,
    text="Calculadora de Matrizes",
    font=("Arial", 14)
)

subtitulo.pack(pady=5)

area_principal = tk.Frame(janela)
area_principal.pack(pady=10)

painel_a = tk.LabelFrame(
    area_principal,
    text="Matriz A",
    padx=15,
    pady=10
)

painel_a.grid(
    row=0,
    column=0,
    padx=10,
    sticky="n"
)

painel_dimensoes_a = tk.Frame(painel_a)
painel_dimensoes_a.pack()

tk.Label(
    painel_dimensoes_a,
    text="Linhas:"
).grid(row=0, column=0, padx=4)

campo_linhas_a = tk.Entry(
    painel_dimensoes_a,
    width=5,
    justify="center"
)

campo_linhas_a.grid(row=0, column=1, padx=4)

tk.Label(
    painel_dimensoes_a,
    text="Colunas:"
).grid(row=0, column=2, padx=4)

campo_colunas_a = tk.Entry(
    painel_dimensoes_a,
    width=5,
    justify="center"
)

campo_colunas_a.grid(row=0, column=3, padx=4)

tk.Button(
    painel_a,
    text="CRIAR MATRIZ A",
    command=criar_matriz_a
).pack(pady=10)

area_a = tk.Frame(painel_a)
area_a.pack()

painel_b = tk.LabelFrame(
    area_principal,
    text="Matriz B",
    padx=15,
    pady=10
)

painel_b.grid(
    row=0,
    column=1,
    padx=10,
    sticky="n"
)

painel_dimensoes_b = tk.Frame(painel_b)
painel_dimensoes_b.pack()

tk.Label(
    painel_dimensoes_b,
    text="Linhas:"
).grid(row=0, column=0, padx=4)

campo_linhas_b = tk.Entry(
    painel_dimensoes_b,
    width=5,
    justify="center"
)

campo_linhas_b.grid(row=0, column=1, padx=4)

tk.Label(
    painel_dimensoes_b,
    text="Colunas:"
).grid(row=0, column=2, padx=4)

campo_colunas_b = tk.Entry(
    painel_dimensoes_b,
    width=5,
    justify="center"
)

campo_colunas_b.grid(row=0, column=3, padx=4)

tk.Button(
    painel_b,
    text="CRIAR MATRIZ B",
    command=criar_matriz_b
).pack(pady=10)

area_b = tk.Frame(painel_b)
area_b.pack()

painel_operacoes = tk.LabelFrame(
    janela,
    text="Operações",
    padx=15,
    pady=10
)

painel_operacoes.pack(pady=10)

tk.Button(
    painel_operacoes,
    text="MOSTRAR A",
    width=18,
    command=mostrar_a
).grid(row=0, column=0, padx=5, pady=5)

tk.Button(
    painel_operacoes,
    text="DETERMINANTE",
    width=18,
    command=calcular_determinante
).grid(row=0, column=1, padx=5, pady=5)

tk.Button(
    painel_operacoes,
    text="VERIFICAR INVERSA",
    width=18,
    command=verificar_inversa
).grid(row=0, column=2, padx=5, pady=5)

tk.Button(
    painel_operacoes,
    text="INVERSA",
    width=18,
    command=calcular_inversa
).grid(row=1, column=0, padx=5, pady=5)

tk.Button(
    painel_operacoes,
    text="TRANSPOSTA",
    width=18,
    command=calcular_transposta
).grid(row=1, column=1, padx=5, pady=5)

tk.Button(
    painel_operacoes,
    text="A × B",
    width=18,
    command=calcular_multiplicacao
).grid(row=1, column=2, padx=5, pady=5)

area_resultado = tk.LabelFrame(
    janela,
    text="Resultado",
    padx=20,
    pady=10
)

area_resultado.pack(
    pady=10,
    fill="x",
    padx=30
)

mensagem = tk.Label(
    janela,
    text="",
    font=("Arial", 11)
)

mensagem.pack(pady=5)

janela.mainloop()