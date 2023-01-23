class Livro:
    def __init__(self, nome, paginas, autor, preco):
        self.nome = nome.title()
        self.paginas = paginas
        self.autor = autor.title()
        self.preco = preco

    def imprimir(self):
        print(f'Nome do Livro: {self.nome} - Paginas: {self.paginas} - Autor: {self.autor} - Valor: {self.preco}')

    def get_preco(self):
        return self.preco

    def set_preco(self, novo_preco):
            if type(novo_preco) == type(str()):
                print("O valor deve ser um FLOAT ou INT!")
            else:
                self.preco = novo_preco

livro = Livro("O principe maquiavel", 179, "nicolau maquiavel", 30.0)
livro.imprimir()
livro.set_preco(777)
livro.imprimir()





