#Exercicio 06 Faça um algoritmo que escreva na tela
#os números de um número inicial a um
#número final. Os números inicial e final
#devem ser informados pelo usuário

def inicialFinal(num, n):
    if(num < n):
        for i in range (num, n+1):     #O +1 é para aparecer o último número solicitado.
            print(i)
    else:
        for i in range (num, n-1, -1): #Esta função else é para o caso de visualização decrescente o número final(n)-1.
            print(i)                   #O -1 é para aparecer a lista corrida.