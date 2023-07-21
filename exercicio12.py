#Exercício 12 Escreva um algoritmo que leia 20
#valores inteiros e ao final exiba
#A) a soma dos números positivos
#B) a quantidade de valores negativos



def exercicio12():

    soma = 0
    contarNegativo = 0

    for i in range(1, 21):
        num = int(input(' {}º número: '.format(i + 1)))
        if (num > 0):
            soma += num
        elif(num < 0):
            contarNegativo += 1
    return ' Positivos: {}  \nContar Negativo: {}'.format(soma, contarNegativo)


