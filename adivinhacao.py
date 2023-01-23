from random import randint
from this import d
from unicodedata import name

def jogar_adivinhacao():
        
    1

    numero_sorteado = randint(1,100)
    tentativas = 0
    pontos = 1000

    #-----------------------Escolha de nivel----------------------
    print('''DIGITE PARA ESCOLHER UM NIVEL:
    \033[32m[ 1 ] FÁCIL\033[m
    \033[33m[ 2 ] MÉDIO \033[m
    \033[31m[ 3 ] DIFÍCIO \033[m''')
    while True:
        nivel = int(input('Qual o nivel escolhido: '))
        #---------------Cada nivel tem uma quantidade de chances diferentes----------
        if (nivel == 1):
            tentativas = 10
            break
        elif(nivel == 2):
            tentativas = 5
            break
        elif(nivel == 3):
            tentativas = 3
            break
        else:
            print("Invalido, digite uma das opções acima! [1,2 ou 3]")
        
    for sorteio in range(1,tentativas +1):
        print('Digite um número entre 1 e 100')
        print('Essa é sua {1}/{0} chances '.format(tentativas,sorteio))
        #print(numero_sorteado)

        aposta = int(input('Qual o seu palpite: '))
        if (aposta < 1) or (aposta > 100) or (aposta < -1):
            print('***VOÇE DEVE DIGITAR UM NUMERO ENTRE 1 E 100***')
            print('VOÇE PERDEU UMA CHANCE!!')
            continue
        
        if (aposta == numero_sorteado):
            print('PARABENS VOCE ACERTOU !!!!!')
            print('E sua pontuaçao foi de {}'.format(pontos))
            break
        elif (aposta > numero_sorteado):
            print('O número digitado esta acima do numero sorteado')
            print('Tente Novamente!!')
        elif (aposta < numero_sorteado):
            print('O número digitado esta abaixo do numero sorteado ')
            print('Tente Novamente!!')

        pontos_perdidos = abs(aposta - numero_sorteado)
        pontos = pontos - pontos_perdidos
    print('O NUMERO SORTEADO ERA:{}'.format(numero_sorteado))
    print('FIM DE JOGO')

if (__name__ == '__main__'):
    jogar_adivinhacao()