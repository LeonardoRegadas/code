leitura = open("valida2.txt", "r", encoding="utf8")
leitura.seek(2)
corte = leitura.read(17)
print(corte)