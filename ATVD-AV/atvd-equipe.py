#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Classes Hospede, Check-in e Check-out e Lista de Hospedes para elas faça:
# uma estrutura que cadastre o hospede
# uma estrutura que gere a lista de hospedes
# uma estrutura que registre o dia da entrada e o dia de saída
# mostre o valor que será pago pela estadia
# você deve validar o CPF, o e-mail do hospede
# o padrão de data 00/00/0000 deve ser verificado tanto no check-in quanto no check-out
# OBS: Faça todas as validações
# OBS: Fique atento aos impedimentos dos métodos
# OBS: Faça a impressão dos elementos
import re 
import datetime
class Hospede():
    def __init__(self,nome = "",cpf = "",email = "",data_nascimento = ""):
        self.nome = nome.title()
        self.cpf = cpf
        self.email = email
        self.data_nascimento = data_nascimento
    
    def valida_cpf(self):
        padrao_cpf =re.compile("[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}")
        verificacao = padrao_cpf.search(self.cpf)
        if verificacao:
            return self.cpf
        else:
            raise ValueError("cpf invalido")
    
    def valida_data(self):
        padrao_data = re.compile("[0-3][0-9][/][0-1][0-9][/][1-2][0][0-2][0-9]")
        verificacao = padrao_data.search(self.data_nascimento)
        if verificacao:
            return self.data_nascimento
        else:
            raise ValueError("data de nascimento invalida")
    
    def valida_email(self):
        padrao_email = re.compile("[A-Za-z0-9.-]+@[A-Za-z0-9_]+.[a-z]{2,3}")
        verificacao = padrao_email.search(self.email)
        if verificacao:
            return self.email
        else:
            raise ValueError("Email inválido")

    def __str__(self):
            return f"Nome do hospede:{self.nome} com data de nascimento:{self.data_nascimento} de cpf:{self.cpf} e email:{self.email}"
 

class CheckIn():
    def __init__(self,data_entrada):
            self.data_entrada = data_entrada

    def registra_entrada(self):
        padrao = re.compile("[0-3][0-9][/][0-2][0-9][/][2][0][0-2][0-9]")
        verficacao = padrao.search(self.data_entrada)
        if verficacao:
            dia = int(self.data_entrada[0:2])
            mes = int(self.data_entrada[3:5])
            ano = int(self.data_entrada[6::])
            data = datetime.date(ano,mes,dia)
  
            self.entrada = data
        else:
            raise  ValueError("data invalida")

    def __str__(self):
        return f"O hospede se registrou no dia {self.data_entrada}"


class CheckOut(CheckIn):
    def __init__(self, data_entrada,data_saida):
        super().__init__(data_entrada)
        self.data_saida = data_saida
    
    def registra_saida(self):
        padrao = re.compile("[0-3][0-9][/][0-2][0-9][/][2][0][0-2][0-9]")
        verficacao = padrao.search(self.data_saida)
        if verficacao:
            dia = int(self.data_saida[0:2])
            mes = int(self.data_saida[3:5])
            ano = int(self.data_saida[6::])
            data = datetime.date(ano,mes,dia)

            self.saida = data
        else:
            raise  ValueError("data invalida")
    
    def calcular(self):
        subtracao_dos_dias = str(self.saida - self.entrada )
        indice = subtracao_dos_dias.find("d")
        numero_de_dias=subtracao_dos_dias[:indice]
        numero_de_dias=int(numero_de_dias)
        self.pagar = numero_de_dias * 75
        print(f"Voce ficou no hotel por {numero_de_dias} dias e tera que pagar R${self.pagar}")


    def __str__(self):
        return f"O hospede se registrou no dia {self.data_entrada} e ficou ate o dia {self.data_saida} e pagou {self.pagar}"


class ListaDeHospedes():
    def __init__(self,lista = None):
        if lista is None:
            self.lista = []
        else:
            self.lista = lista

    def __len__(self):
        print(f"O numero de hospedes na lista é {len(self.lista)}")
        return len(self.lista)
    
    def __getitem__(self,index):
        print(f"O hospede no index {index} é {self.lista[index]}")
        return self.lista[index]

    def __setitem__(self,index,valor):
        if index <= len(self.lista):
            print(f"O hospede de index {index} foi modificado de {self.lista[index]} para {valor}")
            self.lista[index] = valor
        else:
           raise ValueError("o index foi maior que o numero de itens da lista!!!")
    
    def __contains__(self,valor):
        if valor in self.lista:
            print(f"O hospede {valor} esta dentro da lista")
        else:
            raise ValueError(f"O hospede {valor} não esta dentro da lista")

    def append(self,valor):
        self.lista.append(valor)
        print(f"Foi adicionado o hospede '{valor}', sua lista atualizada é {self.lista}")

    def __add__(self,outra_lista):
        print(f"Duas listas foram juntas a lista {self.lista} com {outra_lista.lista}")
        return  ListaDeHospedes(self.lista + outra_lista.lista)

    def __repr__(self):
        return str(self.lista)


pv = Hospede("paulo victor","123.456.789-17","pv@gamil.com","12/11/2003")
sab = Hospede("sabrina","321.654.987-12","sab@gmail.com","13/02/2004")

pv.valida_email()
pv.valida_cpf()
pv.valida_data()
print(pv)

sab.valida_email()
sab.valida_cpf()
sab.valida_data()
print(sab)

a = CheckIn("12/02/2003")
a.registra_entrada()

b = CheckOut("12/02/2003","15/02/2003")
b.registra_entrada()
b.registra_saida()
b.calcular()
print(b)

listas = ["nome:"+"paulo victor cpf:123.456.789-17 data entrada:12/09/2003"," nome:Sabrina cpf:123.456.789-17 data entrada:12/09/2003"]
lista_de_hospedes= enumerate(listas)
for lista in lista_de_hospedes:
    print(lista)
