#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na classe BombaCombustivel abaixo sabemos que é uma bomba de gasolina e:
# atributos: valor_do_litro e quantidade_de_combustivel(na bomba)
# todos atributos encapsulados fortemente (__)
# métodos abaixo:
# abastecer_a_bomba - esse método abastece a bomba para iniciar a venda
# abastecer_veiculo_valor – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer_veiculo_litro – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente
# alterar_valor – altera o valor do litro do combustível
# alterar_quantidade_combustivel – altera a quantidade combustível restante na bomba
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
# OBS: Faça a impressão dos elementos

class BombaCombustivel:
    print("Gasolina esta R$6.00 !!")
    def __init__(self):
        self.valor_do_litro = 6.0
        self.qtd_litros_bomba = 0

    def set_abastecer_a_bomba(self, nova_qtd_bomba):
        if type(nova_qtd_bomba) == type(int()):
            self.qtd_litros_bomba += nova_qtd_bomba
        else:
            print("O valor a se inserir na bomba deve ser inteiro !")
        if nova_qtd_bomba <= 40:
            self.qtd_litros_bomba += nova_qtd_bomba
        else:
            print("A capacidade de litros da bomba e 40L !!")

    def get_bomba(self):
        return self.qtd_litros_bomba

    def abastecer_veiculo_valor(self):
        abastecer = float(input("Digite o valor: "))
        if abastecer <= 40 and abastecer >= 6:
            total_gasolina = (abastecer / self.valor_do_litro)
            print(f"Voce pagou {abastecer} e abasteceu {total_gasolina}Litros")
        else:
            print("??error!!") 

    def abastecer_veiculo_litro(self):
        abastecer = float(input("Digite a qtd de litros para abastecer: "))
        if abastecer <= 40 and abastecer >= 6:
            total_gasolina = (abastecer * self.valor_do_litro)
            print(f"Você abasteceu {abastecer} litros de Gasolina e pagará R$ {total_gasolina}")
        else:
            print("??error!!") 

    def set_altera_valor(self, novo_valor_litro):
        if type(novo_valor_litro) == type(float()):
            self.valor_do_litro += novo_valor_litro
        else:
            print("Valor invalido")

    def alterar_quantidade_combustivel(self, nova_qtd_bomba):
        if type(nova_qtd_bomba) == type(float()):
            self.qtd_litros_bomba += nova_qtd_bomba
            print("Capacidade da bomba alterada !!")
        else:
            print("O valor de ver float")


print("="*20)
bomba = BombaCombustivel()
bomba.abastecer_veiculo_valor()

