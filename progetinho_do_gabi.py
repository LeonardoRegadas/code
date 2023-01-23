import random
class Cadastro():
    def __init__(self, nome):
        self.nome = nome
        self._id = 0

    def gerar_codigo_de_indentificacao(self):
        self._id += random.randint(0,99999999)

    def get_nome(self):
        return self.nome

    def set_nome(self, novo_nome):
        if type(novo_nome) == type(str()):
            self.nome += novo_nome
        else:
            print("Invalido, o nome deve ser uma String !!")

    def __str__(self):
        return (f'>>Seu Nome é: {self.nome} - Seu ID: {self._id}<<')


class Funcionarios(Cadastro):
    def __init__(self, nome, identificacao):
        super().__init__(nome, identificacao)

    def lista_de_funcionarios(self):
        pass


cliente = Cadastro('leo')
print(cliente)
print('='*30)
cliente.gerar_codigo_de_indentificacao()
print(cliente)
cliente02 = Cadastro('maria')
cliente02.gerar_codigo_de_indentificacao()
print(cliente02)