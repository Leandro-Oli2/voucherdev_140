class AlunoAcad:
    def __init__(self, nome, idade, peso, altura, mens = 120.00):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mens = mens
    def imc(self):
        result = self.peso/(self.altura**2)
        print(f"O seu IMC eh de: {result}")
    def valorM(self):
        if(self.idade < 18):
            desc = self.mens*0.3
            self.mens = self.mens - desc
            print(f"Voce recebeu um desconto de R${desc}, sua mensalidade sera {self.mens}")
        else:
            print(f"Sua mensalidade eh: {self.mens}")
        