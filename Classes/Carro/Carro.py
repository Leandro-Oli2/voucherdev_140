class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, consumo, nivel = 0):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.consumo = consumo
        self.nivel = nivel
    def abastecer(self, qtd):
        if(self.nivel <= 100):
            self.nivel = qtd
            print(f"O tanque do seu carro possui {self.nivel} litros")
        else:
            print("Nao eh possivel colocar mais de 100 litros")
    def andar(self, km):
        print(f"O seu carro andou {km} quilometros")
        self.km = km
    def verificaN(self):
        gasto = self.consumo/self.km
        print(f"O seu consum foi de {gasto} por km")
    def imp(self):
        result = (self.valor*2.5)/100
        print(f"Voce Pagara R${result} de imposto")
    

    

