
class IngressoVIP:
    def __init__(self, camarote, open_bar, open_food, estacionamento):
        self.camarote = camarote
        self.openbar = open_bar
        self.openfood = open_food
        self.est = estacionamento
    def pegar_Bebida(self):
        if self.openbar == True:
            bebidas = {
                "Cerveja": 12.90,
                "Caipirinha": 20.78,
                "Pina Colada": 30.78
            }
            for produto, preco in bebidas.items():
                print(f"{produto}: R${preco}")
            esc = input("Informe sua Escolha: ")
            if esc in bebidas:
                print(f"Tome sua {esc}")
            else:
                print("Bebida não encontrada!")
        else:
            print("Voce não tem openBar")

    def acessar_camarote(self):
        if self.camarote == True:
            print("Pode subir Para o Camarote!")
        else:
            print("Voce não tem permissão para acessar o camarote!")
        