from PessoaF import PessoaFisica
from PesssoaJ import PessoaJuridica
pessoa_fisica = PessoaFisica(nome="Maria", telefone="987654321", email="maria@example.com", endereco="Av. B, 456", cpf="123.456.789-00")
pessoa_fisica.negociar()
pessoa_fisica.exibir_cpf()

pessoa_juridica = PessoaJuridica(nome="Empresa XYZ", telefone="555555555", email="contato@empresa.com", endereco="Rua C, 789", cnpj="00.123.456/0001-99")
pessoa_juridica.negociar()
pessoa_juridica.exibir_cnpj()