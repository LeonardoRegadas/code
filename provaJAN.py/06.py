# 6. Siga a sequncia abaixo:
# • peça para o usuário criar um dicionário com 10 frutas e o preço do quilo.
# • imprima o dicionário completo
# • remova a fruta mais cara
# • imprima só os valores
# • imprima os itens com o mesmo valor de preço(se existir)
# • faça uma promoção e altere o valor de duas frutas para 1/3
# • insira duas novas frutas e seus preços
# • salve o dicionário em um arquivo
# • mostre qual fruta mais cara
# • apague o dicionário

frutas = dict ()
for i in range (10):
    fruta = input("Informe uma fruta: ")
    preco = float(input("Informe o preço: "))
    frutas[fruta] = preco

print(frutas)

print('='*20)

maior_valor = max(frutas, key=frutas.get)
print(f'{maior_valor}')
del frutas[maior_valor]
print('='*20)

print(frutas.values())
print('='*20)
