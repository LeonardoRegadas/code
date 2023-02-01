# frutas = {}
# lista_maior = []

# # Criar o dicionário
# frutas_list = input("Insira o nome das frutas separadas por vírgulas: ").split(',')
# precos_list = input("Insira os preços das frutas separados por vírgulas: ").split(',')

# # mostra dict:
# for item in range(len(frutas_list)):
#     frutas[frutas_list[item]] = float(precos_list[item])
# print(frutas)
# print('='*20)

# # valores iguais:



# # mostra so os valores:
# # lista_precos = []
# # for precos in frutas:
# #     lista_precos.append(float(precos_list))
# # print(lista_precos)



# # mostra o maior:
# for valores in precos_list: 
#     lista_maior.append(float(valores))
# maior = max(lista_maior)
# print(f'O maior valor é:{maior}')
# print('='*20)


# # dicionario arquivo:
# arquivo = open("frutas.txt", "a", encoding="utf8")
# for item in range(len(frutas_list)):
#     arquivo.write(frutas_list[item] + ":" + precos_list[item] + "\n")
# arquivo.close()
frutas = dict ()
for i in range (10):
    f = input("diga uma fruta: ")
    v = float(input("diga o preço: "))
    frutas[f] = v

print (frutas) # dicionario de frutas
print (frutas.values()) #apenas os valores
frutas_duplicadas = {}
for i,j in frutas.items():
    frutas_duplicadas.setdefault(j, set()).add(i)
resultado =  [print(j,":",i) for i , j in frutas_duplicadas.items() if len(j) > 1] #imprimir o mesmo valor se  existir

a = 0
for i,j in frutas.items(): #alterando valor de duas frutas
    if a < 2:
        frutas[i] = j * 0.3
        a += 1
    if a == 3:
        break   
print (frutas)

for i in range (2): # adicionado duas frutas no dicionario
    f = input("diga uma fruta: ")
    v = float(input("diga o preço: "))
    frutas[f] = v

print (frutas)

with open ("sacolao_da_aline.txt", "w", encoding="utf-8") as sacola: # escrevendo no arquivo

    [sacola.write(f'{chave}:{valor:.2f} \n') for chave, valor in frutas.items() ]

maior_valor = max(frutas, key = frutas.get) # fruta mais cara
print (f'{maior_valor}:{frutas[maior_valor]}')

del frutas # deletando o dicionario
print (frutas)