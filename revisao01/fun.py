# 1500.00:13
# 1200.00:7
# Faça a verificação de cada funcionário para aplicar o valor de desconto no valor de salario de cada um. Crie um novo arquivo com os funcionários e os novos salários.

funcionarios_1200 = []
funcionarios_1500 = []
desconto_13 = []
desconto_7 = []

arquivo = open("funcionarios.txt", "r", encoding="utf8")
linhas = arquivo.readlines()
for linha in linhas:
        nova_linha = linha.replace("\n", "").split(":")
        salario = (float(nova_linha[1]) >= 1200 and float(nova_linha[1]) < 1500)
        funcionarios_1200.append(nova_linha) if (salario) else funcionarios_1500.append(nova_linha)

# --------------------</>--------------------

arquivo_de_desconto = open("arquivo_de_desconto.txt", "r", encoding="utf8")
linhas = arquivo_de_desconto.readlines()
for linha in linhas:
        nova_linha = linha.replace("\n", "").split(":")
        validacao_de_desconto = (float(nova_linha[1]) >= 7 and float(nova_linha[1]) < 13)
        desconto_7.append(float(nova_linha[1])/100) if (validacao_de_desconto) else desconto_13.append(float(nova_linha[1])/100)

# --------------------</>--------------------

arquivo_salario = open("arquivo_salario.txt", "a", encoding="utf8")
for valor in funcionarios_1200:
    valor_salario = float(valor[1])
#<--calcula e escreve no arquivo-->
    calculo = float(valor_salario * (desconto_7[0]))
    valor[1] = float(valor[1]) - calculo
    arquivo_salario.write(f"{valor[0]} - R${valor[1]:.2f}\n")

for valor in funcionarios_1500:
    valor_salario = float(valor[1])
#<--calcula e escreve no arquivo-->
    calculo = float(valor_salario * (desconto_13[0]))
    valor[1] = float(valor[1]) - calculo
    arquivo_salario.write(f"{valor[0]} - R${valor[1]:.2f}\n")

arquivo.close()
arquivo_de_desconto.close()
arquivo_salario.close()