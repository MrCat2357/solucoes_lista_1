import math as mt

R = 3
r = 2
n = 3
a = mt.pi

def f(h):
    return a*(h**3)-3*R*a*(h**2)+90
def df(h):
    return 3*a*(h**2)-2*3*R*a*h

def mtd_newton_raphson(r,n):
    
    h = r     #aproximação inicial
    iteracao = 0
    
    for iteracao in range (n):
        h = h - f(h)/df(h)
       
        erro_percentual = abs((h - 2.026905728) / h) * 100
        print(f"Iteração {iteracao + 1}: h = {h}, Erro Percentual = {erro_percentual:.6f}%")
        
        iteracao += 1

    
    return h  
    
resultado = mtd_newton_raphson(r, n)
print(f"Resultado final: {resultado}")