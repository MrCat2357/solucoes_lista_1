#Método do ponto falso
import math as mt
import numpy as np

q = 20
g = 9.81
erro = 0.00001    #erro menor que 1%
r = 0.5       #extremidade inferior do intervalo de solução
s = 2.5         #extremidade superior do inteervalo de solução
n = 10

def b(x):
    return 3 + x
def a(x):
    return 3*x + 0.5*(x**2)

def f(x):
    return ((q**2)*b(x))/(g*(a(x)**3))-1

def mtd_falsa_posicao(r, s, erro, n): # r e s são as extremidades do intervalo,
                                    # erro representa a aproximação desejada
                                    # n representa a quantidade de iterações que eu quero
    if f(r)*f(s) >= 0:
        print("Neste intervalo não há mudança de sinal")
        return None

    iteracao = 0
    while (s-r)/2 > erro and iteracao < n:
        x_falso = r - (f(r)*(s-r))/(f(s)-f(r))
        f_x_falso = f(x_falso)

        if f_x_falso == 0:
             return x_falso
        elif f_x_falso*f(r) < 0:
             s = x_falso
        else: 
             r = x_falso
        iteracao += 1

    return (r+s)/2

resultado = mtd_falsa_posicao(r, s, erro, n)

if resultado is not None:
    print(f"Aproximação da raiz: {resultado:.6f}") #aproximação do resultado com 6 casas decimais

else:
    print("O método não convergiu para uma solução.")
