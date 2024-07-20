class PassagemAviao:
    def __init__(self, preco, assento, portaoD, checkin):
        self.portaoD = portaoD
        self.checkin = checkin
        self.preco = preco
        self.assento = assento
    def decolar(self):
        print(f"Avião decolando do portão {self.portaoD}")