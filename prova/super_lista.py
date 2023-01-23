#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Crie uma classe InteiroSet
# Cada objeto de InteiroSet pode armazenar inteiros no intervalo de 0 a 999. 
# O conjunto de objetos é representado por uma lista
# Um construtor sem argumento inicializa a lista vazia 
# Faça os seguintes métodos: 
# Método para unir listas
# Método para alterar o valor de um elemento 
# Método para mostrar o tamanho da lista
# Método insereElemento insere um novo elemento inteiro k em um conjunto
# Método toSetString que retorna uma string contendo a lista de números separados por espaço. Inclua somente os elementos que estão presentes na lista
# Método que verifique se existe igualdade entre duas listas 
# Crie duas listas e faça as devidas implementações
# OBS: Veja a possibilidade de utilizar os métodos mágicos
# OBS: Faça todas as validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça as impressões necessárias

class InteiroSet():
    def __init__(self, lista=None):
        if lista is None:
            self.lista = []
        else:
            self.lista = lista

#verifica o tamanho da lista
    def __len__(self):
        return len(self.lista)

#retorna o item selecionando a posicao
    def __getitem__(self, index):
        return self.lista[index]

#altera o item na posicao desejada
    def __setitem__(self, index, valor):
        if valor >= 0 and valor < 1000:
            if index <= len(self.lista):
                self.lista[index] = valor
            else:
                raise IndexError()
        else:
            raise ValueError("O valor deve ser de 0 a 999")
        
#verifica se o valor/item ta na lista
    def __contains__(self, valor):
        return valor in self.lista


#append - adiciona valor
    def append(self, valor):
        if valor >= 0 and valor < 1000:
            self.lista.append(valor)
        else:
            raise ValueError("O valor deve ser de 0 a 999")

#junta duas listas
    def __add__(self, outra_lista):
        return InteiroSet(self.lista + outra_lista.lista)

# verifica se tem igualdade
    def __eq__(self, other):
        return self.lista == other.lista

#representacao/imprimir
    def __repr__(self):
        return str(self.lista)

super_lista = InteiroSet()
super_lista.append(0)
super_lista.append(999)
super_lista.append(4)
print(super_lista)
super_lista[2] = 100
print(super_lista[2])
print(super_lista)
print(8 in super_lista)
print(100 in super_lista)
print('='*20)
super_lista2 = InteiroSet()
super_lista2.append(13)
super_lista2.append(29)
super_lista2.append(100)
print(super_lista2)
print("tamanho da lista:", len(super_lista2))
print(super_lista + super_lista2)
print(super_lista == super_lista2)