from prettytable import PrettyTable
import math

e = 0.9
r = 3
n = 40
a = math.pi

# Criando uma instância da classe PrettyTable
tabela = PrettyTable()

# Adicionando colunas à tabela
tabela.field_names = ["valores de pi/x", "valores de y"]


for i in range(1, 31):
    def f(y):
        return y - e*math.sin(y) - a/i
    def df(y):
        return 1 - math.cos(y)

    def mtd_newton_raphson(r,n):
        
        y = r     #aproximação inicial
        iteracao = 0
        
        for iteracao in range (n):
            y = y - f(y)/df(y)
                    
            iteracao += 1

        
        return y  
        
    resultado = mtd_newton_raphson(r, n)
    tabela.add_row([i, resultado])

# Imprimir a tabela formatada
print(tabela)






