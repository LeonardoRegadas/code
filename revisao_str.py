import re

class ValidaCPF():
    def __init__(self, numero_cpf):
        self.numero_cpf = str(numero_cpf)
        if self.cpf_valido(numero_cpf):
            self.cpf = numero_cpf
        else:
            raise ValueError("CPF invalido")

    def formata_cpf(self):
        parte_um = self.cpf[:3]
        parte_dois = self.cpf[3:6]
        parte_tres = self.cpf[6:9]
        parte_quatro = self.cpf[9:]
        return (f'{parte_um}.{parte_dois}.{parte_tres}-{parte_quatro}')

    def __str__(self):
        return self.formata_cpf()

    def cpf_valido(self, numero_cpf):
        padrao = re.compile("([0-9]{3}.?){2}[0-9]{3}-?[0-9]{2}")
        busca = padrao.search(numero_cpf).group()
        if busca:
            if len(numero_cpf) == 11:
                return True
            else:
                return False
        else:
            return False


meu_cpf = ValidaCPF("12345678910")
print(meu_cpf)
