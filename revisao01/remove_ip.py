octeto_cortado = []
ip =  open("ips.txt", "r", encoding="utf8")
linhas = ip.readlines()
for linha in linhas:
    nova_linha = linha.replace("\n", " ").split(".")
    del nova_linha[3]
    del nova_linha[2]
    del nova_linha[1]
    octeto_cortado.append(int(nova_linha[0]))
for x in octeto_cortado:
    if x > 254:
        print(f"{x} - INVALIDO!!! ")
    else:
        print(f"{x} - VALIDO")
print('='*30)
print(sorted(octeto_cortado))
ip.close()