class Pessoa:
    def __init__(self, nome, tel, email, endereco):
        self.nome = nome
        self.tel = tel
        self.email = email
        self.endereco = endereco
    def negociar(self):
        print(f"{self.nome} esta Negociando!")