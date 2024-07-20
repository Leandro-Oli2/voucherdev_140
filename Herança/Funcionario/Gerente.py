from Funcionario import Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario, senha):
        super().__init__(nome, matricula, salario)
        self.senha = senha
    
    def gerenciar_equipe(self):
        print(f"Gerente {self.nome} gerenciando a equipe.")