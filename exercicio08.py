#Exercicio 08 Ler números inteiros e, ao final, apresente a
#soma de todos os números lidos


def ler10inteirosSoma():
    soma = 0                                          # Instanciar a variáevel
    for i in range(1, 11, 1):
        num = int(input(' {}° número: '.format(i)))
        soma += num
    return soma