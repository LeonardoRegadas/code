# regular expresion 101
# fixo = -
# celular = .
import re

lista_fixo = []
lista_celular = []

# with open("contatos.txt", "r") as contatos:
#     linhas = contatos.read()

# with open("arquivo_modificado", "w") as arquivo2:
#     validacao = re.findall(r'(?\d{2})?\s?\d{4,5}[-.]?\d{4}', contatos)
#     for numero in validacao:
#         if re.search(r'-', numero):
#             arquivo2.write(f'{numero} - FIXO')
#         else:
#             arquivo2.write(f'{numero} - CELULAR')

# import re

# # Abrir arquivo de entrada
# with open('contatos.txt', 'r') as arquivo_entrada:
#     # Abrir arquivo de saída
#     linhas = arquivo_entrada.read()
#     with open('saida.txt', 'w') as arquivo_saida:
#         # Percorrer linhas do arquivo de entrada
#         for linha in arquivo_entrada:
#             # Separar chave e valor
#             chave, valor = linha.split(':')
#             # Verificar se o valor é um número de telefone
#             if re.match(r'\d{2}[-.]\d{4,5}[-.]\d{4}', valor):
#                 # Verificar se é fixo ou móvel
#                 if re.match(r'\d{2}[-]\d{4,5}[-]\d{4}', valor):
#                     tipo = 'fixo'
#                 else:
#                     tipo = 'móvel'
#                 # Escrever no arquivo de saída
#                 arquivo_saida.write(f'{chave}: {valor} ({tipo})\n')


import re
with open('contatos.txt', 'r', encoding="utf8") as contatos:
    ler = contatos.readlines()
    padrao = re.compile()
    for i in ler:
        if padrao.search(i):
            i = i.replace('\n', '')
            print(f'{i}valido')
