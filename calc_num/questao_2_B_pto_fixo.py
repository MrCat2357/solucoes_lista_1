# MÉTODO DO PONTO FIXO
import math as mt
import numpy as np

x_0 = 3  # valor inicial
n = 3    # número máximo de iterações

def f(x):
    return 2*x**3-11.7*x**2+17.7*x-5

def g(x):
    return (2*x**3-11.7*x**2-5)/(-17.7) # (nessa etapa o grande bizu é 
                                        # isolar o x da eq original)



def mtd_pto_fixo(x_0, n): 

    x = x_0
    iteracao = 0

    for iteracao in range(0,n):
        x = g(x)
        iteracao += 1

    return x

resultado = mtd_pto_fixo(x_0, n)

if resultado is not None:
    print(f"Aproximação da raiz: {resultado:.6f}") #aproximação do resultado com 6 casas decimais

else:
    print("O método não convergiu para uma solução.")

erro = abs(resultado - 3.56316)/3.56316
print (f'o erro percentual vale: {erro:.5f}')