class Circulo:
    def __init__(self, raio, pi = 3.14):
        self.raio = raio
        self.pi = pi
    def imprimirRaio(self):
        print(f"O raio do circulo eh {self.raio}")
    def calcArea(self):
        result = self.pi*(self.raio**2)
        print(f"A area do circulo eh {result}")
    def calcCircuferencia(self):
        result = 2*self.pi*self.raio
        print(f"A circuferencia do circulo eh: {result}")
