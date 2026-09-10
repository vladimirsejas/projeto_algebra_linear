import numpy as np


def determinante(matriz):
    return np.linalg.det(np.array(matriz))


def possui_inversa(matriz):
    return not np.isclose(determinante(matriz), 0)


def inversa(matriz):
    return np.linalg.inv(np.array(matriz))


def transposta(matriz):
    return np.array(matriz).T


def multiplicar(A, B):
    return np.array(A) @ np.array(B)