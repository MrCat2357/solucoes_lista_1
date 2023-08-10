import numpy as np
import math as mt

def norma(x, y):
    f = max(abs(x), abs(y))
    a = min(abs(x), abs(y))

    for n in range(1, 4):  # Correção: Usar range(1, 4) para percorrer de 1 a 3
        b = (a / f) ** 2
        c = b / (4 + b)
        f = f + 2 * c * f
        a = c * a

    return f

# Obter as coordenadas do usuário
coordenadas = []
valores = input("Digite os valores das coordenadas (separados por espaço): ").split()
coordenadas = [float(valor) for valor in valores]
print("Coordenadas:", coordenadas)

# Calcular a norma para cada par de coordenadas
for i in range(len(coordenadas) - 1):
    norma_result = norma(coordenadas[i], coordenadas[i + 1])
    print(f"Norma Euclidiana entre ({coordenadas[i]}, {coordenadas[i+1]}): {norma_result}")


