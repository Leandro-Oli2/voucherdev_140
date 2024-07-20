class Funcionario:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario
        self.pontos = []
    def bater_ponto(self, ponto):
        self.pontos.append(ponto)