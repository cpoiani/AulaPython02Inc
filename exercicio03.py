#Exercicio 03
# Determinar se um número é par ou
#ímpar e positivo ou negativo


def parImpar(num):
    if(num % 2 == 0):
        return 'Par'
    else:
        return 'Ímpar'

def positivoNegativo (num):
    if(num >= 0):
        return 'Positivo'
    else:
        return 'Negativo'