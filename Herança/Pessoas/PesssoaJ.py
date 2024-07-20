from Pessoas import Pessoa  

class PessoaJuridica(Pessoa):
    def __init__(self, nome, telefone, email, endereco, cnpj):
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
    
    def exibir_cnpj(self):
        print(f"CNPJ da empresa {self.nome}: {self.cnpj}")