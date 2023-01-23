from adivinhacao import jogar_adivinhacao
from forca import jogar_forca


def escolher_jogo():
    print('*'*26)
    print('ESCOLHA UM JOGO PARA JOGAR')
    print('*'*26)


    while (True):
        print('''QUAL JOGO VOCÊ DESEJA JOGAR? 
        [ 1 ] Adivinhção
        [ 2 ] Forca ''')

        jogo_selecionado = int(input('Qual a sua opção: '))

        if (jogo_selecionado == 1):
            jogar_adivinhacao()
            break
        elif(jogo_selecionado == 2):
            jogar_forca()
            break
        else:
            print('Digite uma opção correta! ')

if(__name__ == '__main__'):
    escolher_jogo()