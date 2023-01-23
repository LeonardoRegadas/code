class ListaCustomizada():
    def __init__(self, lista=None):
        if lista is None:
            self.lista = []
        else:
            self.lista = lista

#tamanho da lista
    def __len__(self):
        return len(self.lista)

#retorna o item selecionando a posicao
    def __getitem__(self, index):
        return self.lista[index]

#altera o item na posicao desejada
    def __setitem__(self, index, valor):
        if index <= len(self.lista):
            self.lista[index] = valor
        else:
            raise IndexError()

#verifica se o valor/item ta na lista
    def __contains__(self, valor):
        return valor in self.lista

#dunder do append
    def append(self, valor):
        self.lista.append(valor)

#junta duas listas
    def __add__(self, outra_lista):
        return ListaCustomizada(self.lista + outra_lista.lista)

#representacao/imprimir
    def __repr__(self):
        return str(self.lista)

minha_lista = ListaCustomizada()
minha_lista.append(1)
minha_lista.append(2)
minha_lista.append(4)
minha_lista.append(7)
minha_lista.append(76)
print(minha_lista)
print(len(minha_lista))
print(minha_lista[4])
print('='*20)
minha_lista[4] = 100
print(minha_lista[4])
print(minha_lista)
print(8 in minha_lista)
print(100 in minha_lista)
print('='*20)
minha_lista2 = ListaCustomizada([23, 45])
minha_lista2.append(1345)
minha_lista2.append(298)
print(minha_lista2)
print(minha_lista + minha_lista2 + minha_lista)