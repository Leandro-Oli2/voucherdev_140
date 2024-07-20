from Triangulo import Triangulo

lado1 = float(input("Digite o lado A: "))
lado2 = float(input("Digite o lado B: "))
lado3 = float(input("Digite o lado C: "))
tri = Triangulo(lado1, lado2, lado3)
tri.calcP()
tri.getMaiorLado()