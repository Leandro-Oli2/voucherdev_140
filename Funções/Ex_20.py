import random
lista=[]
for i in range(6):
    nom = input("Digite um nome: ")
    lista.append(nom)

def sorteioal(num):
    x = random.choice(num)
    print(f"O primeiro Aluno a apresentar eh: {x}")
sorteioal(lista)