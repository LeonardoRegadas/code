frutas = {}
lista_maior = []

# Criar o dicionário
frutas_list = input("Insira o nome das frutas separadas por vírgulas: ").split(',')
precos_list = input("Insira os preços das frutas separados por vírgulas: ").split(',')

# mostra dict:
for item in range(len(frutas_list)):
    frutas[frutas_list[item]] = float(precos_list[item])
print(frutas)
print('='*20)

# valores iguais:



# mostra so os valores:
# lista_precos = []
# for precos in frutas:
#     lista_precos.append(float(precos_list))
# print(lista_precos)



# mostra o maior:
for valores in precos_list: 
    lista_maior.append(float(valores))
maior = max(lista_maior)
print(f'O maior valor é:{maior}')
print('='*20)


# dicionario arquivo:
arquivo = open("frutas.txt", "a", encoding="utf8")
for item in range(len(frutas_list)):
    arquivo.write(frutas_list[item] + ":" + precos_list[item] + "\n")
arquivo.close()