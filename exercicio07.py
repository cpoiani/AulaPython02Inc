#Exercicio 07 Escrever um algoritmo que gera e
#escreva os números ímpares entre 100 e
#200 na ordem crescente


def cemDuz():
    for i in range(100, 200):
        if(i % 2 == 1):
            print(i)