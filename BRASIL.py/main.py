# from CPF_CNPJ import Documento
# from validate_docbr import CNPJ

# #cpf_um = Cpf("15316264754")
# #print(cpf_um)

# exemplo_cnpj = "35379838000112"
# #exemplo_cpf = "11111111112"

# #cnpj = CNPJ()
# #print(cnpj.validate(exemplo_cnpj))
# documento = Documento.cria_documento(exemplo_cnpj)
# print(documento)
from Telefones import TelefonesBr
import re

telefone = "0302126481234"
telefone_objeto = TelefonesBr(telefone)

#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao,telefone)
#print(resposta.group())

print(telefone_objeto)