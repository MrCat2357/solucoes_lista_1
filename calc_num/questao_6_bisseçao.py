import math
r_e = float(input("escolha um valor para a constante de Reynolds:"))
erro = 0.000005 #erro menor que 1%
r = 0.00001        #extremidade inferior do intervalo de solução
s = 0.1        #extremidade superior do inteervalo de solução
n = 50  

def f(x):
    return (1/math.sqrt(x))-4*math.log10(r_e*math.sqrt(x))+0.4
def mtd_bisec(r, s, erro, n): # r e s são as extremidades do intervalo,
                            # erro representa a aproximação desejada
                            # n representa a quantidade de iterações que eu quero
    if f(r)*f(s) >= 0:
        print("a função não apresenta raízes nesse intervalo")
        return None
    
    iteracao = 0
    while (s - r)/2 > erro and iteracao < n:
        t = (r+s)/2
        if f(t) == 0:
            return t
        elif f(t) * f(r) < 0:
            s = t
        else:
            r = t
        iteracao += 1
    return (r+s)/2

resultado = mtd_bisec(r, s, erro, n)

if resultado is not None:
    print(f"Aproximação da raiz: {resultado:.6f}") #aproximação do resultado com 6 casas decimais

else:
    print("O método não convergiu para uma solução.")

