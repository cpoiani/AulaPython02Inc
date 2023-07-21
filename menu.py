
from exercicio01 import dobro
from exercicio01 import triplo
from exercicio02 import salario
from exercicio03 import parImpar
from exercicio03 import positivoNegativo
from exercicio04 import somaCem
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import inicialFinal
from exercicio07 import cemDuz
from exercicio08 import  ler10inteirosSoma
from exercicio09 import exercicio09
from exercicio10 import exercicio10
from exercicio11 import exercicio11
from exercicio12 import exercicio12
from exercicio13 import exercicio13
from exercicio14 import exercicio14
from exercicio15 import preenchernomeExercicio15
from exercicio16 import eleicao
from exercicio17 import
from vetores import preencherVetor
from vetores import consultarVetor
from vetores import apagarPosicao





def mostrarMenu():
    print(' Escolha uma das opções abaixo: ' +
            '\n0 SAIR '              +
            '\n01. Exercício 01 ' +
            '\n02. Exercício 02 ' +
            '\n03. Exercício 03'  +
            '\n04. Exercício 04'  +
            '\n05. Exercício 05'  +
            '\n06. Exercício 06'  +
            '\n07. Exercício 07'  +
            '\n08. Exercício 08'  +
            '\n09. Exercício 09'  +
            '\n10. Exercício 10'  +
            '\n11. Exercício 11'  +
            '\n12. Exercício 12'  +
            '\n13. Exercício 13'  +
            '\n14. Exercício 14'  +
            '\n15. Exercício 15'  +
            '\n16. Exercício 16'  +
            '\n17. Exercício 17'  +
            '\n18. Exercício 18'  +
            '\n19. Exercício 19'  +
            '\n20. Exercício 20'  +
            '\n21. Preencher Vetor' +
            '\n22. Consultar Vetor' +
            '\n23. Apagar posição Vetor')



def operacao(): #Chamar o método de cima
    opcao = 1
    while( opcao != 0):
        mostrarMenu()
        opcao = int(input(' Digite aqui o número da opção escolhida: '))           #Coletar a opção do usuário
        if(opcao == 0):
            print (' Obrigado! ')
        elif(opcao == 1):
            print('\nExercício 01')
            num = int(input('Informe um número: '))
            print(dobro(num))
            print(triplo(num))
        elif(opcao == 2):
            print('\nExercício 02')
            num = int(input('Informe um número: '))
            print(salario(num))
        elif (opcao == 3):
            print('\nExercício 03')
            num = int(input('Informe um número: '))
            print(parImpar(num))
            print(positivoNegativo(num))
        elif (opcao == 4):
            print('\nExercício 04')
            print(' A soma do número um ao cem é: {}'.format(somaCem()))
        elif (opcao == 5):
            print('\nExercício 05')
            num = int(input(' Informe um número: '))
            n = coletarPositivo()
            tabuada(num, n)
        elif (opcao == 6):
            print('\nExercício 06')
            num = int(input(' Informe o número inicial: '))
            n = int(input('Informe o número final: '))
            inicialFinal(num, n)
        elif (opcao == 7):
            print('\nExercício 07')
            print('\n Lista dos números ímpares de 100 a 200 completa!'.format(cemDuz()))
        elif (opcao == 8):
            print('\nExercício 08')
            print(' A soma entre 1 a 10 é: {}'.format(ler10inteirosSoma()))
        elif (opcao == 9):
            print('\nExercício 09')
            print(' O resultado da soma dos números digitados é: {}'.format(exercicio09()))
        elif (opcao == 10):
            print('\nExercício 10')
            print(exercicio10())
        elif (opcao == 11):
            print('\nExercício 11')
            print(exercicio11())
        elif (opcao == 12):
            print('\nExercício 12')
            print(exercicio12())
        elif (opcao == 13):
            print('\nExercício 13')
            exercicio13()
        elif (opcao == 14):
            print('\nExercício 14')
            print(exercicio14())
        elif (opcao == 15):
            print('\nExercício 15')
            print(preenchernomeExercicio15())
        elif (opcao == 16):
            print('\nExercício 16')
            print(eleicao())
        elif (opcao == 17):
            return
        elif (opcao == 18):
            return
        elif (opcao == 19):
            return
        elif (opcao == 20):
            return
        elif(opcao == 21):
            num= int(input(' Informe o tamanho do vetor: '))
            preencherVetor(num)
        elif(opcao == 22):
            num = int(input(' Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif(opcao == 23):
            posicao = int(input(' Informe a posição que deseja apagar'))
            apagarPosicao(posicao - 1)
        else:
            print(' Opção escolhida não é válida! ')