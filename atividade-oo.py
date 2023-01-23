class Aluno():
    def __init__(self, nome, curso, tempo_dormir):
        self.nome = nome.title()
        self.curso = curso.title()
        self.tempo_dormir = 0

    def get_curso(self):
        return self.curso

    def set_curso(self, novo_curso):
        if type(novo_curso) == type(str()):
            self.curso = novo_curso  
        else:
            print("O curso deve ser uma str !!")

    def get_tempo(self):
        return self.tempo_dormir

    def estudar(self, estudar):
        self.tempo_dormir += estudar
        print(f"Estudando os conteudos do curso:{self.curso}")

    def dormir(self):
       self.tempo_dormir -= 8
       print("dormindo")

    def imprimir(self):
        print(f'Nome:{self.nome} - Curso:{self.curso}')
        if self.tempo_dormir >= 8:
            print(f"Estou com muito sono, estou a {self.tempo_dormir} horas sem dormir")
        else:
            print("Cuida na farra!")


aluno = Aluno("leo", "back-end", 0)
aluno.estudar(8)
aluno.imprimir()
aluno.dormir()
aluno.imprimir()
aluno.set_curso("oi")
aluno.imprimir()

