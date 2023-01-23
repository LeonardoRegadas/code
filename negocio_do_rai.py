planop=('Lavagem Completa - Limpeza interior - Troca de oleo - Revisão Basica')
planoc=('Lavagem Completa - Limpeza interior')
class LavaJato():
    def __init__(self, cliente, carro, tipo_lavagem):
        self._cliente = cliente.upper()
        self.carro = carro.upper()
        self.tipo_lavagem = tipo_lavagem

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, novo_nome):
        if type(novo_nome) == type(str()):
            self._cliente += novo_nome
        else:
            raise ValueError("O novo nome deve ser uma str !!")


    def get_carro(self):
        return self.carro

    
    def set_carro(self, nv_carro):
        if type(nv_carro) == type(str()):
            self.carro += nv_carro
        else:
            raise ValueError("O novo nome do carro deve ser uma str !!")

    @property
    def lavagem(self):
        return self.tipo_lavagem

    @lavagem.setter
    def lavagem(self, nova_lavagem):
        if type(nova_lavagem) == type(str()):
            self.tipo_lavagem += nova_lavagem
        else:
            raise ValueError("O tipo de lavagem deve ser uma str !!")

    def __str__(self):
        return (f'Nome:{self._cliente} - Carro:{self.carro}')

    

class LavagemPremium(LavaJato):
    def __init__(self, cliente, carro, plano_premium):
        super().__init__(cliente, carro)
        self._plano_premium = plano_premium

    def __str__(self):
        return (f'Voce e o cliente:{self._cliente}/n Carro:{self.carro}/n Plano Premium:{planop}')
    

class LavagemNormal(LavaJato):
    def __init__(self, cliente, carro, lavagem_comum):
        super().__init__(cliente, carro)
        self._lavagem_comum = lavagem_comum

    def __str__(self):
        return (f'Voce e o cliente:{self._cliente}/n Carro:{self.carro}/n Plano Premium:{planoc}')


cliente = LavaJato('leo', 'honda civic', 'premium')
print(cliente)
cliente = LavagemPremium('leo', 'honda civic', 'premium')
