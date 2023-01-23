

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def extrato(self):
    print("Saldo de {} do titular {}".format(self.saldo, self.titular))

def saca(self,valor):
    self.saldo -= valor

def deposita(self, valor):
    self.saldo += valor
    

