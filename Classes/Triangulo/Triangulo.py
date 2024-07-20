class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    def calcP(self):
        result = self.ladoA + self.ladoB + self.ladoC
        print(f"O Perimetro do triangulo eh {result}")
    def getMaiorLado(self):
        if self.ladoA >= self.ladoB and self.ladoA >= self.ladoC:
            print("O lado A é o maior")
        elif self.ladoB >= self.ladoA and self.ladoB >= self.ladoC:
            print("O lado B é o maior")
        else:
            print("O lado C é o maior")
