# Algortimo de Moler-Morrison para o cálculo da norma euclideana

import numpy as np
import math as mt

x = float(input('digite o valor de x:'))
y = float(input('digite o valor de y:'))


def norma(x,y):
   
    f = max(abs(x),abs(y))
    a = min(abs(x),abs(y))

    for n in (1,2,3):
        b = (a/f)**2
        c = b/(4+b)
        f = f + 2*c*f
        a = c*a

    return f

print(f"norma desse vetor é: {norma(x,y)}")