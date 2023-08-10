import matplotlib.pyplot as plt
import numpy as np
import math as mt
# Graphics Method

x_0 = 0  # valor inicial
n = 3    # número máximo de iterações
k_1 = 50 # Kg/s²
k_2 = 0.04 # Kg/(s²*m^0,5)
m = 0.09 # Kg
g = 9.81 # m/s²
h = 0.45 # m

def b(x):
    return ((2*k_2*x**(5*2))/5)+0.5*k_1*x**2
def a(x):
    return m*g*x+m*g*h

def f(x):
    return b(x)-a(x)

def grafico(m, n, p = 200):
    x = np.linspace(m, n, p)
    y = f(x)
    raizes = []
    raiz = 0

    for i in range(len(x)-1): # len mede o tamanho do intervalo que x está varrendo
        if (y[i]*y[i+1] < 0): # aplicação do teorema de Bolzano
            raiz = (x[i]*abs(f(x[i+1])) + x[i+1]*abs(f(x[i]))) / \
                (abs(f(x[i+1])) + abs(f(x[i]))) # essa operação iterativa da raiz é uma média ponderada
        raizes.append(round(raiz, 5)) #append para armazenar a raiz no bloco [] e
                                    # round para arredondar em 5 casas decimais o valor da raiz
    

        if (y[i] == 0):
            raiz = x[i]
            raizes.append(round(raiz, 5))
    
    print(raizes)
    plt.plot(x,a(x))
    plt.plot(x,b(x))
    plt.plot(x,y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

grafico(-5, 5)    