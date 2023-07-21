#Exercicio 10 Escreva um algoritmo que calcule a
#média dos números digitados pelo
#usuário, se eles forem pares. Termine a
#leitura se o usuário digitar zero 0

def exercicio10():
        media = 0
        num = 1
        soma = 0
        i = 0
        while(num != 0):
                num = int(input(' Informe um número: '))

                if (num % 2 == 0):
                    soma += num
                    i += 1
                else:
                    print('Digite apenas números pares')


        media = soma/(i - 1)
        return 'A soma é {} e a média é {}'.format(soma, media)

