import random

def jogar():
    imprime_abertura()
    palavras_secreta = contem_palavras()
    letras_acertadas = inicalizar_letras_acertadas(palavras_secreta)
    print(letras_acertadas)
    
    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavras_secreta):
            marca_chute_correto(chute, letras_acertadas, palavras_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        imprime_win()
    else:
        imprime_loser(palavras_secreta)

def desenha_forca(erros):
    print("  ___     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("|__         ")
    print()

def imprime_win():
    print("Parabéns, você ganhou!")
    print("       _____      ")
    print("      '.=====.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         .' '.        ")
    print("        '-------'       ") 

def imprime_loser(palavras_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavras_secreta))
    print('     ░░░░░░░░░░░░░░░░░     ')
    print('   │░░░░░░░░░░░░░░░░░░░│   ')
    print('   │░░░░░░░░░░░░░░░░░░░│   ')
    print('  ░└┐░░░░░░░░░░░░░░░░░┌┘░  ')
    print('  ░░└┐░░░░░░░░░░░░░░░┌┘░░  ')
    print('  ░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░  ')
    print('   ░│██████▌░░░▐██████│░   ')
    print('   ░│▐███▀▀░░▄░░▀▀███▌│░   ')
    print('   ─┘░░░░░░░▐█▌░░░░░░░└─   ')
    print('   ░░░    ░░▀█▀░░    ░░░   ')
    print('        ─┘░░░░░░░   └─     ')
    print('     ░░  ─┬┬┬┬┬┬┬─  ░░     ')
    print('     ░░░ ┬┼┼┼┼┼┼┼┬ ░░░     ')
    print('      ░░░└┴┴┴┴┴┴┴┘░░░      ')
    print('        ░░░░░░░░░░░        ')

def marca_chute_correto(chute, letras_acertadas, palavras_secreta):
    index = 0
    for letra in palavras_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

def pede_chute():
    chute = input("Qual Letra : ")
    chute = chute.strip().upper()
    return chute
    
def inicalizar_letras_acertadas(palavras):
    return['_' for l in palavras]

def contem_palavras():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero = (random.randrange(0,len(palavras)))
    palavras_secreta = palavras[numero].upper()
    return palavras_secreta
    
def imprime_abertura():
    print("***********")
    print("**Bem vindo ao jogo da Forca!**")
    print("***********")

if(__name__ == "__main__"):
    jogar()
