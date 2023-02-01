# 5. você deve solicitar o nome e o salario, armazenar em um arquivo no formato de DIC, apicar 6% de desconto se o salario for maior que R$1.500,00 e mostrar o DIC na tela ao final de tudo.

funcionarios = dict ()

nome = input("Nome do Funcionario: ")
salario = float(input("Salario: "))
funcionarios[nome] = salario

with open('FUNCIONARIOS_QUESTAO_05.txt', 'a', encoding='utf8') as arquivo:
    if salario > float(1500.0):
        calculo = float(salario * (6/100))
        adiciona_desconto = salario = float(salario) - calculo
        arquivo.write(f"{nome} : R${adiciona_desconto:.2f}\n")
    else:
        arquivo.write(f"{nome} : R${salario:.2f}\n")

print('='*20)

with open('FUNCIONARIOS_QUESTAO_05.txt', 'r', encoding='utf8') as arquivo:
    ver = arquivo.read()
    print(ver)






    
    