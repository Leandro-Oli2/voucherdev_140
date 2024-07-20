graus = float(input("Digite os graus em celsius: "))
def convert(g):
    f = g*(9.0/5.0) + 32.0
    print(f"{g} em fahrenheit eh {f}")
convert(graus)