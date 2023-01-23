try:
    print(2 + 2)#'casa'
except TypeError:
    print('ops deu erro')


print('='*20)
try:
    print(x)
except:
    print('variavel x nao esta definida')
finally:
    print("o try except nao esta finalizado")


print('='*20)
try:
    print('hello')
except:
    print('algo deu errado')
else:
    print('nada deu errado')


print('='*20)