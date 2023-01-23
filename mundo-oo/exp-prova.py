class Livro:
    def __init__(self, nome, qtd_paginas, autor):
        self.nome = nome
        self.paginas = qtd_paginas
        self.autor = autor

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if type(novo_preco) == type(float()):
            self.__preco = novo_preco
        else:
            print("deve ser float")

    def __str__(self):
        return f' O {self.__class__.__name__} {gibi.nome} do autor {gibi.autor} tem {gibi.paginas} paginas e custa R${gibi.get_preco()} '

    #self.__class__.__name__ (isso e o nome da CLASS) 

    preco = property(get_preco, set_preco)

gibi = Livro("Turma da monica", 22, "Mauricio de Sousa")
print("="*20)
gibi.set_preco(7.50)
print(gibi.get_preco())
print("="*20)



class bolacha():
    def __init__(self,um):

class recheado(bolacha):
    def __init__(self, um,dois):
        super().__init__(um)

class crack(recheado):
    def __init__(self, um, dois,tres):
        super().__init__(um, dois)