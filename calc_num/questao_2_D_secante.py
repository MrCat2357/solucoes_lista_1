# MÉTODO DA SECANTE

x_0 = 4 # valor inicial de x da iteração
x_1 = 3 # segundo valor de x da iteração 
n = 3   # qtd de iterações

def f(x):
    return 2*x**3 - 11.7*x**2 + 17.7*x - 5

def mtd_secantes(x_0, x_1, n):

    iteracao = 0
    for iteracao in range(0,n):
        x_new = x_1 - (f(x_1)*(x_1 - x_0))/(f(x_1) - f(x_0))
        x_0 = x_1
        x_1 = x_new
        
        iteracao += 1   

    return x_1    

resultado = mtd_secantes(x_0, x_1, n)
print (resultado)

erro = abs(resultado - 3.56316)/3.56316
print (f'o erro percentual vale: {erro:.5f}')