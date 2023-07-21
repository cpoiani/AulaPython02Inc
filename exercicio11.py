#Exercício 11 Escreva um algoritmo que leia valores
#inteiros e encontre o maior e o menor
#deles. Termine a leitura se o usuário
#digitar zero (0)


def exercicio11():
    num = 1
    maior = 0
    menor = 0
    flag = False  #Valor lógico, binário

    while (num != 0):
         num = int(input(' Informe um número: '))
         if(num!=0):
            if(flag == False):
                maior = num    # Instanciei os valores menores e maiores.
                menor = num
                flag = True      # Só roda a primeira vez, ligado e desligado.

            if(num > maior):
                maior = num

            if(num < menor):
                menor = num

    return 'O número maior é: {} e o número menor é {}'.format(maior, menor)
