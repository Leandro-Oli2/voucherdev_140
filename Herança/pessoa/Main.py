from Aluno import Aluno
from Professor import Professor

##ALUNO
nom = input("Digite o nome do aluno: ")
id = int(input("Digite a idade do aluno: "))
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))

al = Aluno(nom, id, n1, n2)
x = al.calc_media()
al.estudar()
print(f"Media do aluno {nom}: {x}")

##Professor
nom = input("Digite o nome do Professor: ")
id = int(input("Digite a idade do Professor: "))
form = input("Digite a formacao do Professor: ")
disc = input("Digite a disciplina do Professor: ")
car = input("Digite a carga horaria do Professor: ")
sal = float(input("Digite o salario do Professor: "))

p1 = Professor(nom, id, form, disc, car, sal)
p1.salario()
p1.carga()
