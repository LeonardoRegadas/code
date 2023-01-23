def contaVogais(frase):
    vogais = {'a','e','i','o','u','A','E','I','O','U'}
    nVogais = 0 
    for letra in frase:
        if letra in vogais:
            nVogais += 1
    print(f"Quantidade de Vogais:{nVogais}")
    return None

#programa
lida = input("Diga uma frase: ")
contaVogais(lida)

