valor = open('valores.txt', 'r')
pag_valor = open('pagamentos.txt', 'w')

for linha in valor:
    nome=input("aa:")
    pag_valor.write(nome + ":" + linha + "\n")

valor.close()
pag_valor.close()

pag_valor = open("pagamentos.txt", "r")
for linha in pag_valor:
    print(linha)
