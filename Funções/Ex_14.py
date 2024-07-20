km = int(input("Digite a distancia em km percorridos: "))
litros = float(input("A quantidade de litros consumidos: "))

def calculo_gasto(km, litros):
    tot = km/litros
    if(tot <= 8 ):
        print("Gasta Muito!")
    elif(tot > 8 and tot <=15):
        print("Economico!")
    elif(tot > 15):
        print("Super Economico")

calculo_gasto(km, litros)