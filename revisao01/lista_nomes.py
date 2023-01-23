vogais = ["a", "e", "i", "o", "u", "y", "w", "A", "E", "I", "O", "U", "Y", "W"]
lista = open("lista_nomes.txt", "r", encoding="utf8")
linhas = lista.readlines()
nomes_cortados = []
for nomes in linhas:
    for i in vogais:
        nomes_cortados.append(nomes.strip().lower().replace(i, " "))
    print(nomes_cortados)
