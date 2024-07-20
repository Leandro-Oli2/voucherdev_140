class Brinquedos:
    def __init__(self, nome, cor, tamanho, preco):
        self.nome = nome
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
    def brincar(self):
        print(f"Estou Brincando com {self.nome}")

class BuzzLightyear(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, tem_asa):
        super().__init__(nome, cor, tamanho, preco)
        self.tem_asa = tem_asa
    
    def brincar(self):
        print(f"{self.nome} voa ao infinito e além!")

class Woody(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, tem_chapu):
        super().__init__(nome, cor, tamanho, preco)
        self.tem_chapu = tem_chapu
    
    def brincar(self):
        print(f"{self.nome} está laçando!")

class Carrinho(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, tipo):
        super().__init__(nome, cor, tamanho, preco)
        self.tipo = tipo
    
    def brincar(self):
        print(f"{self.nome} está correndo pela pista!")

class Jessie(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, tem_chapu):
        super().__init__(nome, cor, tamanho, preco)
        self.tem_chapu = tem_chapu
    
    def brincar(self):
        print(f"{self.nome} está montando seu cavalo!")

class Rex(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, rugido):
        super().__init__(nome, cor, tamanho, preco)
        self.rugido = rugido
    
    def brincar(self):
        print(f"{self.nome} está rugindo alto!")

class Slinky(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, elasticidade):
        super().__init__(nome, cor, tamanho, preco)
        self.elasticidade = elasticidade
    
    def brincar(self):
        print(f"{self.nome} está se esticando!")

class SrCabeçaDeBatata(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, acessorios):
        super().__init__(nome, cor, tamanho, preco)
        self.acessorios = acessorios
    
    def brincar(self):
        print(f"{self.nome} está mudando seus acessórios!")

class Alien(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, tres_olhos):
        super().__init__(nome, cor, tamanho, preco)
        self.tres_olhos = tres_olhos
    
    def brincar(self):
        print(f"{self.nome} está indo para o espaço!")

class Betty(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, guitarra):
        super().__init__(nome, cor, tamanho, preco)
        self.guitarra = guitarra
    
    def brincar(self):
        print(f"{self.nome} está tocando guitarra!")

class BalanoAlvo(Brinquedos):
    def __init__(self, nome, cor, tamanho, preco, sela):
        super().__init__(nome, cor, tamanho, preco)
        self.sela = sela
    
    def brincar(self):
        print(f"{self.nome} está Carregando seus Amigos!")
