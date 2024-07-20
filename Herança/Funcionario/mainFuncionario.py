from Vendedor import Vendedor
from Gerente import Gerente
from Funcionario import Funcionario

funcionario1 = Funcionario(nome="Carlos", matricula="12345", salario=3000.00)
funcionario1.bater_ponto(1)
print(f"Pontos de {funcionario1.nome}: {funcionario1.pontos}")

vendedor1 = Vendedor(nome="Ana", matricula="54321", salario=2500.00, comissao=0.1)
vendedor1.bater_ponto(1)
vendedor1.bater_meta()


gerente1 = Gerente(nome="Pedro", matricula="99999", salario=5000.00, senha="senha123")
gerente1.bater_ponto(1)
gerente1.gerenciar_equipe()