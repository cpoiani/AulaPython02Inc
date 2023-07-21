#Exercicio 05 Construa um programa que exiba a
#tabuada de 1 até N



def tabuada(num,n):
    for i in range(1, n+1):
        print(' {} * {} = {} '.format(num, i, num * i))

def coletarPositivo():                               #Função complementar para impedir a entrada de números negativos
    num = float(input(' Informe o número final: '))
    while(num <= 0):
        print(' Valores negativos são inválidos, informe um número positivo')
        num = float(input(' Informe o número final '))
    return num