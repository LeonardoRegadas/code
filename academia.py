class Aluno:
    def _init_(self, identificador, nome, idade, peso, altura):
        self.__identificador = identificador
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura
        self.imc = 0
    
    
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self):
        return self._idade
    
    @property
    def peso(self):
        return self._peso
    @peso.setter
    def peso(self):
        return self._peso
    
    @property
    def altura(self):
        return self._altura
    @altura.setter
    def altura(self):
        return self._altura
    
    def calcular_imc(self):
        self.imc = self.peso/(self.altura*self.altura)
        return self.imc
    
    def imprime(self):
        print(f'Id: {self.__identificador} - Nome: {self.nome} - Idade: {self.idade} - Peso: {self.idade} - Altura: {self.altura} - Imc: {self.calcular_imc():.2f}')
        
aluno = Aluno(500, "Leo", 17, 56, 1.75)
aluno.imprime()