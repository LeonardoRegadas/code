consoantes = {'B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','X','Z'}
nomes = []
convertido = {}
apelido = {}
with open("lista_nomes.txt", "r", encoding="utf8") as meus_nomes:
    lista_nomes = meus_nomes.readlines()
    for linha in lista_nomes:
        nova_linha = linha.replace('\n', '').upper()
        corta_linha = list(nova_linha)
        convertido = set(corta_linha)
        apelido = convertido.intersection(consoantes)
        if len(apelido) == 3:
            nomes.append(str(apelido))
        elif len(apelido) >= 4:
            apelido.remove(list(apelido)[0])    
            nomes.append(str(apelido))
    print('\n'.join(map(str, nomes)))

#pegar lista de nomes e montar um apelido para o nome utilizando 3 consoantes do mesmo
# import re
# with open('lista_nomes.txt', 'r', encoding='utf8') as nomes:
#     for nome in nomes:
#         sem_vogal = (re.sub('[AÁÃÂEÉÊIÍOÓÔÚUaáâãeéêiíoóôuú]','',nome.strip()))
#         if len(sem_vogal) >= 3: 
#             print(sem_vogal[0:3])