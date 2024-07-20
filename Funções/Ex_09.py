pi = 3.141592
raio = float(input("Digite o raio do cilindro: "))
alt = float(input("Digite a altura do cilindro: "))
def calc(r, pi, alt):
    v = pi*(r**2)*alt
    print(f"O volume do cilindro eh: {v}")
calc(raio, pi, alt)