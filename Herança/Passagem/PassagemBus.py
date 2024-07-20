class PassagemBus:
    def __init__(self, preco, assento, placa, leito):
        self.placa = placa
        self.leito = leito
        self.preco = preco
        self.assento = assento
    def abastecer(self):
        print(f"Ônibus de placa {self.placa} sendo abastecido")
    