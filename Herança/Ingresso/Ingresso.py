class Ingresso:
    def __init__(self, preco, setor):
        self.preco = preco
        self.setor = setor
    def alterar_preco(self, new):
        self.preco = new
        print(f"Novo Preco: {self.preco}")
    def mostrar_setor(self):
        print(f"O setor Escolhido eh: {self.setor}")