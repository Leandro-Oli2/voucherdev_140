from AlunoAcad import AlunoAcad

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))
peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))

al = AlunoAcad(nome, idade, peso, alt)
al.imc()
al.valorM()

