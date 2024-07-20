from Aluno import Aluno
print("=-=-=-=-=-=-=-=-=-=-=-=")
nome = input("Digite o nome do aluno: ")
ra = int(input("Digite o ra: "))
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

aluno1 = Aluno(nome, ra, n1, n2, n3, n4)
aluno1.situation()