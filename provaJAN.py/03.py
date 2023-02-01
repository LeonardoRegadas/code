# 3. você deve solitiar o nome e o numero de telefone, armazenar em um arquivo no formato de DIC, validar o numero informado e mostrar o DIC na tela ao final de tudo.(99)3333-2222 ou (99)98888.4444 (VALIDOS)

import re
numeros = dict ()

nome = input("Nome: ")
numero = input("Numero de telefone: ")
numeros[nome] = numero

with open('NUMEROS.txt', 'a', encoding="utf8") as contatos:
    padrao = re.compile(r'\d{2}[-.]\d{4,5}[-.]\d{4}')
    for i in numero:
        if padrao.search(i):
            i = i.replace('\n', '')
            contatos.write(f'Nome:{nome} : Numero:{numero}')
        else:
            contatos.write('Numero Invalido')
            print('Numero Invalido')
            break

with open('NUMEROS.txt', 'r', encoding="utf8") as contatos:
    ver = contatos.read()
    print(ver)