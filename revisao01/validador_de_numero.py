# numero = [int(input("informe um numero: "))]
# numero_par = list(filter(lambda x: x%2 == 0,numero))
# print(numero_par)

# filter:
# filter é para validacao
# para verificar se for impar tem que ser 1 na igualdade
# ele so adiciona o numero na lista se ele for par


# numero = [11, 20, 30, 12, 45, 100]
# adiciona_imposto = list(map(lambda x: x + x*0.15, numero))
# print(adiciona_imposto)
# map:
# map e para execusao
# se adicionar o x+x vc adiciona o valor mais o imposto


# filter e condicional:
# alunos = [{"nome": "Aurelice", "matricula": 1000},
# {"nome": "Sara", "matricula": 1100},
# {"nome": "Aline", "matricula": 1200}]
# verifica_matricula = list(filter(lambda x: x["matricula"] > 1100, alunos))
# print(verifica_matricula)

# lista_compras = [{"descricao" : "agua", "preco" : 2.00},
#                   {"descricao" : "leite", "preco" : 3.00},
#                   {"descricao" : "carne", "preco" : 18.00},
#                   {"descricao" : "pizza", "preco" : 9.00},
#                   {"descricao" : "chocolate", "preco" : 6.50}]

# lista_compras_com_imposto = list(map(lambda produto: {"Descrição": produto["Descrição"], "Preço": produto["Preço"] * 1.10}, lista_compras))
# for item in lista_compras_com_imposto:
#     print(f'- { item["Descrição"]}, Preço: {item["Preço"]:.2f}')

# lista_numeros = []
# for c in range(5):
#     c = int(input("Informe um valor:"))
#     lista_numeros.append(c)
# print('='*20)
# maior_q_vinte  = list(filter(lambda c: c>20, lista_numeros))
# print(f'Maiores que vinte:{maior_q_vinte}')

# maior = max(lista_numeros)
# menor = min(lista_numeros)

# print('='*20)
# print(f"O dobro do maior numero é:{maior*2}")
# print('='*20)
# print(f'O triplo do menor numero é:{menor*3}')

# lista_vazia = []
# lista_compras = [{"descricao" : "agua", "preco" : 2.00},
#                   {"descricao" : "leite", "preco" : 3.00},
#                   {"descricao" : "carne", "preco" : 18.00},
#                   {"descricao" : "pizza", "preco" : 9.00},
#                   {"descricao" : "chocolate", "preco" : 6.50}]
# for item in lista_compras:
#     lista_vazia.append(item["preco"])

# maior = max(lista_vazia)#pega o maior item da lista
# menor = min(lista_vazia)#pega o menor item da lista

# print(f'O maior valor é: {maior}')
# print(f"O menor valor é: {menor}")
# print("="*20)
# print(f"Todos os valores da lista:\n{lista_vazia}")
# print("="*20)

# # <- mostra todos os itens na lista de compras ->
# for valor in lista_compras:
#     print(f'- {valor["descricao"]} = R$ {valor["preco"]:.2f}')

# -----------------------</>------------------------

# op_ternario:
# <expressao1> if <condicao> else <expressao2>
# user_log = True # False
# if user_log == True:
#     msg = "Usuario logado com sucesso !!"
# else:
#     msg = "Login Incorreto, verifique seu usuario ou senha !!"
# print(msg)

# -----------------------</>------------------------

# user_log = True # False
# msg = 'Usuario Logado com sucesso!' if (user_log) else "Login Incorreto, verifique seus dados !!"
# print(msg)


# -----------------------</>------------------------

idade = input("Informe sua idade: ")
if not idade.isnumeric():
    print("Voce precisa digitar somente numeros")
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    e_adolecente = (idade > 12 and idade < 18)
    msg = "Voce e de maior!!!"if e_de_maior else "Voce é adolecente" if e_adolecente else "voce é crianca"
    print(msg)

# -----------------------</>------------------------

