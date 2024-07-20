from Funcionario import Funcionario

func = Funcionario("Leandro", "Oliveira Candido", 100, 50.0)
func.nomeCompleto()
x = func.calcSalario()
print(f"O seu salario eh: {x}")
func.incremento(20)
x = func.calcSalario()
print(f"O seu novo salario eh: {x}")