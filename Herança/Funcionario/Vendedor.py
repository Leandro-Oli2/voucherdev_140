from Funcionario import Funcionario
class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario, comissao):
        super().__init__(nome, matricula, salario)
        self.comissao = comissao
    
    def bater_meta(self):
        print(f"Vendedor {self.nome} batendo meta!")