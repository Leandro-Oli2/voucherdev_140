from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, formacao, disciplina, carga_h, sal):
        super().__init__(nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.__cargah = carga_h
        self.__salario = sal
    def salario(self):
        print(f"O salario do Professor eh {self.__salario}")
    def carga(self):
        print(f"A carga horaria do professor eh: {self.__cargah}")