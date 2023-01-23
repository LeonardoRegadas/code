

class ContaCorrente():
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f'>> Codigo {self.codigo} - Saldo {self.saldo}<<'


conta_do_leo = ContaCorrente(15)
print(conta_do_leo)
print('='*20)
conta_do_leo.deposita(500)
print(conta_do_leo)
print('='*20)
conta_da_dani = ContaCorrente(23232)
conta_da_dani.deposita(1000)
print(conta_da_dani)
print('='*20)
contas = [conta_do_leo, conta_da_dani]
for conta in contas:
    print(conta)
