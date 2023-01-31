#  utilizando expressões regulares, Escreva um programa que, dada uma palavra, verifique se ela existe no arquivo dom_casmuro.txt se sim mostre quantas vezes ela existe. Você não pode aceitar numeros e nem palavras menores que três letras no input.

# import re

# palavra = str(input("Informe uma palavra: ")).lower()
# if len(palavra) < 3:
#     print("A palavra deve ter pelo menos mais de 3 letras")
# else:
#     padrao = ("[a-z]{1}")
#     resposta = re.search(padrao, palavra)

#     arquivo = open("dom_casmuro.txt", "r", encoding="utf8")
#     linhas = arquivo.readlines()
#     qtd = 0

#     for linha in linhas:
#         nova_linha = linha.lower()
#         if palavra == nova_linha:
#             qtd += 1
            
# print(f"Quantidade de vezes que essa palavra - {palavra} - aparece : {qtd}")
# arquivo.close()

#importa a biblioteca re para usar expressões regulares.
import re
# Abre o arquivo dom_casmuro.txt como arquivo e define o encoding como UTF-8.
with open('dom_casmuro.txt', 'r', encoding='UTF-8') as arquivo:
    # Lê o conteúdo do arquivo e armazena na variável texto.
    texto = arquivo.read()

# Solicita ao usuário que digite uma palavra para procurar no arquivo e armazena na variável busca_palavra.
busca_palavra = input('Digite uma palavra para procurar no arquivo: ')

# Verifica se a entrada tem pelo menos 3 caracteres.
if len(busca_palavra) < 3:
    print('A entrada deve ter pelo menos 3 caracteres.')
# Se a entrada for válida, executa o código abaixo.
else:
    # Usa a expressão regular para encontrar todas as ocorrências da palavra no texto.
    buscar = re.findall(r"\b" + busca_palavra.lower() + r"\b", texto.lower())
	# fronteira do caractere
    # Conta o número de correspondências.
    contador = len(buscar)
    # Imprime o número de ocorrências da palavra no arquivo ou uma mensagem de que a palavra não existe no arquivo.
    print(f"A palavra '{busca_palavra}' aparece {contador} vezes no arquivo.") if contador>0 else print(f"A palavra '{busca_palavra}' não existe no arquivo.")
