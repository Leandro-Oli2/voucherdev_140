class Passagem:
    def __init__(self, preco):
        self.preco = preco
        self.assento = ""
    def alterar_preco(self, new):
        self.preco = new
        print(f"Novo Preco: {self.preco}")
    def escolher_assento(self,ass):
        self.assento = ass
