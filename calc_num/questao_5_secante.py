import math as mt
import numpy as np

p = mt.pi
f_value = 1.25
e_0 = 8.85*(10**(-12))
a = 0.9
q = 2*(10**(-5))
n = 10  
x_0 = 1
x_1 = 0.1
y_0 = 2
y_1 = 1

def f(x):
    return f_value*4*p*e_0*((x**2 + a**2)**(3/2)) - (q**2)*x

def mtd_secantes(x_0, x_1, n):

    iteracao = 0
    for iteracao in range(0,n):
        x_new = x_1 - (f(x_1)*(x_1 - x_0))/(f(x_1) - f(x_0))
        x_0 = x_1
        x_1 = x_new
        
        iteracao += 1   

    return x_1    

resultado = mtd_secantes(x_0, x_1, n)
print (f"raíz 1 = {resultado}")

resultado_2 = mtd_secantes(y_0, y_1, n)
print (f"raíz 2 = {resultado_2}")



