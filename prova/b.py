#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na Super classe Funcionario você faz:
# atributos: nome, tempo de empresa, salario(encapsular), faturamento mensal
# Nas Subs classes Vendedor e Supervisor você faz:
# atributos: valor_da_comissao, comissao_especial
# Os métodos devem obedecer o polimorfismo
# métodos abaixo:
# calcula_comissao_especial - esse método calcula o percentual de comissão pelo tempo de empresa maior igual 5 anos 3%, maior igual a 10 anos 6% e maior que 15 anos 9%
# calcula_comissao_especial - esse método calcula o percentual de comissão pelo faturamento mensal, até 15mil/mês 3%, maior igual a 15mil 6%
# OBS: Deve ser criado o POLIMORFISMO do ambiente
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos

class Funcionario:
    def __init__(self, nome, tempo_de_empresa, __salario, faturamento_mensal, valor_da_comissao, comissao_especial):
        self.nome = nome
        self.tempo_empresa = tempo_de_empresa
        self.salario = __salario
        self.faturamento_mensal = faturamento_mensal
        self.valor_da_comissao = valor_da_comissao
        self.comissao_especial = comissao_especial

    def calcula_valor_da_comissao(self):
        if self.tempo_empresa >= 5:
            print(self.tempo_empresa * (3/100) * 100)#multipliquei por 100 para ficar o numero inteiro, pois ele estava em decimal !!
        elif self.tempo_empresa >= 10:
            print(self.tempo_empresa * (6/100) * 100)
        elif self.tempo_empresa >= 15:
            print(self.tempo_empresa * (9/100) * 100)
        else:
            print("??error!!")

    def calcula_comissao_especial(self):
        if self.faturamento_mensal < 15000:
            print(self.faturamento_mensal * (3/100))
        elif self.faturamento_mensal >= 15000:
            print(self.faturamento_mensal * (6/100))

    def get_comissao(self):
        return self.valor_da_comissao

    def set_comissao(self, nova_comissao):
        if type(nova_comissao) == type(float()):
            self.valor_da_comissao += nova_comissao
            print(nova_comissao)
        else:
            print("o valor deve ser float")

    def get_comissao_especial(self):
        return self.comissao_especial
    
    def set_comissao_especial(self, nova_especial):
        if type(nova_especial) == type(float()):
            self.comissao_especial += nova_especial
            print(nova_especial)
        else:
            print("o valor deve ser float")

    def imprimir(self):
        print(f'Seu relatorio: Nome:{self.nome} - Tempo na empresa:{self.tempo_empresa} - Salario:{self.salario} - Faturamento:{self.faturamento_mensal} comissao:{self.valor_da_comissao} esp - {self.comissao_especial}')

class Vendedor(Funcionario):
    def __init__(self, nome, tempo_de_empresa, __salario, faturamento_mensal, valor_da_comissao):
        super().__init__(nome, tempo_de_empresa, __salario, faturamento_mensal)
        self.valor_da_comissao = valor_da_comissao
        

class Supervisor(Funcionario):
    def __init__(self, nome, tempo_de_empresa, __salario, faturamento_mensal, valor_da_comissao, comissao_especial):
        super().__init__(nome, tempo_de_empresa, __salario, faturamento_mensal, valor_da_comissao, comissao_especial)
        self.valor_da_comissao = valor_da_comissao
        self.comissao_especial = comissao_especial


advogado = Supervisor("Leo", 5, 12000.0, 70000.0, 10, 100)
print("="*20)
advogado.calcula_valor_da_comissao()
print("="*20)
advogado.calcula_comissao_especial()
print("="*20)
advogado.set_comissao_especial(3.0)
print("="*20)
advogado.set_comissao(3000.0)
advogado.imprimir()
