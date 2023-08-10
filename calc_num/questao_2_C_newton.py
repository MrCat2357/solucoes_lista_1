# MÉTODO DE NEWTON-RAPHSON
r = 3         # aproximação inicial
n = 3    # máxima iteração

def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5

def df(x):         # definição da derivada da função
    return 6*x**2 - 23.4*x + 17.7

def mtd_newton_raphson(r,n):
    
    x = r     #aproximação inicial
    iteracao = 0
    
    for iteracao in range (n):
        x = x - f(x)/df(x)
        iteracao += 1

    
    return x  
    

resultado = mtd_newton_raphson(r,n)
print (resultado)

erro = abs(resultado - 3.56316)/3.56316
print (f'o erro percentual vale: {erro:.5f}')


