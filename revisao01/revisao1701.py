# import os
# # try:
# #     arq = open("valida.txt", "w", encoding="utf8")
# #     arq.write("Não e um teste de escrita")
# # finally:
# #     arq.close()


# # with open("valida2.txt", "w", encoding="utf8") as meu_arquivo:
# #     meu_arquivo.write("Novo teste de Não é o python")
# #-----------------------------------------------------------

# pessoas = ["João", "Maria", "Pedro"]

# for pessoa in pessoas:
#     with open(f"carta_{pessoa}.txt", "w", encoding="utf-8") as arquivo:
#         arquivo.write(f"Ola {pessoa},\n\n")
#         arquivo.write("Espero que esteja tudo bem com você.\n\n")
#         arquivo.write("Estou escrevendo para lhe desejar um ótimo dia.\n\n")
#         arquivo.write("Espero que você possa aproveitar ao máximo o dia de hoje.\n\n")
#         arquivo.write(f"Atenciosamente,\n\n")
#         arquivo.write("Seu amigo\n")

# with open(f"carta_{pessoa}.txt", "r", encoding="utf-8") as arquivo:
#     print(arquivo.read())

# # -------------------------------------------------------

# # os.remove("valida.txt") - remove o arquivo
# # os.rename("valida2.txt", "alterado.txt") - renomeia o arq

# lista = os.listdir() - mostra arqs/pastas no diretorio
# print(len(lista)) faz parte do listdir
# print('='*20)
# # print(lista[10]) - mostra a atvd pelo index
