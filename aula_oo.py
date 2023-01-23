class Felino():
    cor_do_pelo = ""
    juba = False
    fome_do_felino = 0
    
    def imprimir(self):
        print("Meu nome é: ", self.nome)
        print("Minha pelo é: ", self.cor_do_pelo)
        if self.juba == False:
            print("Eu não tenho juba!")
        else:
            print("Eu tenho juba!")
        if self.fome_do_felino >= 50:
            print("Estou com pouca fome")
        else:
            print("Estou com fome !")
    
    def alimentar(self, comida):
        self.fome_do_felino += comida
        
    def get_nome(self):
        print("Entrou no metodo GETTER")
        return self.__nome

    def set_nome(self, novo_nome):
        print("Entrou no metodo SETTER")
        if type(novo_nome) == type(str()):
            self.__nome = novo_nome
        else:
            print("Nome deve ser uma STRING!")
    
    nome = property(get_nome, set_nome)
