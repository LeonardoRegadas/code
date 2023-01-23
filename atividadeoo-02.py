class Carro:
    def __init__(self, modelo_do_carro, cor, potencia_motor, consumo, litros_no_tanque, velocidade):
        self.modelo = modelo_do_carro.upper()
        self.cor = cor.upper()
        self.potencia = potencia_motor
        self.consumo = consumo
        self.litros_tanque = litros_no_tanque
        self.velocidade = velocidade

    def imprimir(self):
        print(f'Carro: {self.modelo} - Cor: {self.cor} - Potencia: {self.potencia} - Consumo: {self.consumo} - L: {self.litros_tanque} - V: {self.velocidade}')

    def get_pintar(self):
        return self.cor

    def set_pintar(self, nova_cor):
        lista_de_cores = ["vermelho", "azul", "verde", "amarelo", "chumbo", "prata", "branco"]
        print(f'ESCOLHA UMA DESSAS CORES: {lista_de_cores}')
        if nova_cor in lista_de_cores:
            self.cor = nova_cor.title()
        else:
            print("Desculpe nao temos essa cor")


carro = Carro("Fusca", "prata", 1000, 14, 10, 250)
carro.set_pintar("leo")
carro.imprimir()
    
    