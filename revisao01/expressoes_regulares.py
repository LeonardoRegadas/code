import re

palavra = "teste"

string = "Este é um teste de expressões regulares"

print(re.search(r"teste", string)) # encontra a primeira ocorrencia e retorna a posiçao
print(re.findall(r"teste", string)) # encontra todas as ocorrencias da palavra e retorna uma lista delas
print(re.sub(r"teste", "ABCD", string)) # encontra a palavra e substitui por uma nova em todas as ocorrencias////////parecido com o replace em listas
print(re.sub(r"teste", "ABCD", string, count=1)) # encontra a palavra e substitui por uma nova somente na primeira ocorrencia////////parecido com o replace em listas

regexp = re.compile(r"teste")
print(regexp.search(string))
print(regexp.findall(string))
# print(regexp.sub("ABCDE", string))

#expressão de metaclasses | = OU  
#re.findall(r"palavra|outra|letra", texto)

#expressão de metaclasses . = Qualquer caracter (com exceção da quebra de linha)
#re.findall(r"palavra|nam..ado"), texto)
#>>>["palavra", "namorado", "(alguma palavra com nam..ado e dois caracteres quaisquer)"]

#expressão de metaclasses [] = Ele cria um conjunto de caracteres
#re.findall(r"[Jj]oão|[(]gabriel[)]|[Mm]aria")
#>>>[João, joao, (gabriel), Maria, maria]

#expressão de metaclasses
#re.findall(r"jOãO|mArIa", texto, flags=re.IGNORECASE) = Ele faz com que ignore todos os parametros de Letras Maiusculas, minusculas
#>>>[João, joão, Maria, maria]