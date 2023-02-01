# 2. você deve verificar quantas vezes a palavra digitada aparece no texto e informar em qual linha ela foi encontrada

import re
with open('dom_casmuro.txt', 'r', encoding='UTF-8') as arquivo:
    texto = arquivo.read()
    linha = arquivo.readline()

palavra = input('Digite uma palavra: ')
if len(palavra) < 3:
    print('A entrada deve ter pelo menos 3 letras.')
else:
    busca = re.findall(r"\b" + palavra.lower() + r"\b", texto.lower())
    aparicoes = len(busca)
    print(f"A palavra '{palavra}' aparece {aparicoes} vezes no arquivo")
