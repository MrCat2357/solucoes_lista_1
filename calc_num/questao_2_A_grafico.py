### SOLUÇÃO POR MÉTODO GRÁFICO ###
import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return 2*(x**3)-11.7*x**2

def f2(x):    
    return -17.7*x+5

def grafico(m, n, p=1001):
    x = np.linspace(m, n, p)
    y1 = f1(x)
    y2 = f2(x)
    
    # Encontrar os pontos de interseção com o média aritmética
    pontos_intersecao = []
    for i in range(len(x)-1):
        if (y1[i] - y2[i]) * (y1[i+1] - y2[i+1]) < 0:
            ponto_x = (x[i] + x[i+1]) / 2
            ponto_y = (y1[i] + y2[i]) / 2
            pontos_intersecao.append((ponto_x, ponto_y))
    
    plt.plot(x, y1, label='f1(x)')
    plt.plot(x, y2, label='f2(x)')
    
    # Plotar pontos de interseção como marcadores vermelhos no gráfico
    for ponto in pontos_intersecao:
        plt.scatter(ponto[0], ponto[1], color='red')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

grafico(0.1, 5)

