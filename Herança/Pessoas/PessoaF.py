from Pessoas import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cpf):
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
    
    def exibir_cpf(self):
        print(f"CPF de {self.nome}: {self.cpf}")