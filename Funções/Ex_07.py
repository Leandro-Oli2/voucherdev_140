pi = 3.14
raio = float(input("Digite o raio da esfera: "))
def calc(r, pi):
    v = (4/3)*pi + r**3
    print(f"O volume da esfera eh: {v}")
calc(raio, pi)