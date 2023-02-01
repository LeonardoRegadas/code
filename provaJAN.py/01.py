# 1. você deve listar os arquivos do seu diretorio padrão salvando em um arquivo e informar quantos arquivos existem no mesmo.

import os

with open('diretorio.txt', 'a', encoding='utf8') as arquivo:
    lista = os.listdir()
    tamanho_lista = (len(lista))
    arquivo.write(f'ESSES SÃO OS ARQUIVOS DO DIRETORIO:\n{lista}\n')
    arquivo.write(f'QUANTIDADE EXISTENTE:{tamanho_lista} ARQUIVOS')

