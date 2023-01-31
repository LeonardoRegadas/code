#funcoes lambda:
multiplicar = lambda x:x*2
print(multiplicar(10))#vc deve colocar o valor que quer multiplicar !!

absoluto = lambda x,y:abs(x-y)<3#verifica se o calculo do abs e menor que 3(<)
print(absoluto(2,4))

alteracoes = lambda x,n:x*n+x/n#calculos
print(alteracoes(10,1))

print('='*30)

#funcoes como parametro:

#funcoes-map:
# usar list para printar
#pow - calcula a potencia de 2 numeros
base_numericas = [2, 4, 6, 8, 10]
aplicaveis = [1, 2, 3, 4, 5]
numeros_potenciais = list(map(pow, base_numericas, aplicaveis))
print(numeros_potenciais)

meus_numeros = [10, 15, 21, 33, 42, 55]
map_numeros = list(map(lambda x:x*2+8,meus_numeros))
print(map_numeros)

#---------------------------------------------->

#funcao filter:
#diferenca de numeros/remove
numeros = [0,4,7,2,1,0,9,3,5,6,8,0,3]
numeros = list(filter(lambda x : x != 0, numeros))
print(numeros)

nomes = ["leo", "marcelo", "cassio", "gabi", "ademastror", "vini"]
print(list(filter(lambda x : x[0].lower() in "aeiou", nomes)))