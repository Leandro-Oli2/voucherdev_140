class Transporte:
    def __init__(self, capacidade_passageiros, velocidade_maxima):
        self.capacidade_passageiros = capacidade_passageiros
        self.velocidade_maxima = velocidade_maxima
    
    def mover(self):
        print(f"Transporte em movimento com velocidade máxima de {self.velocidade_maxima} km/h")

class Terrestre(Transporte):
    def __init__(self, capacidade_passageiros, velocidade_maxima, tipo_terreno):
        super().__init__(capacidade_passageiros, velocidade_maxima)
        self.tipo_terreno = tipo_terreno
    
    def __str__(self):
        return f"Transporte Terrestre - Capacidade: {self.capacidade_passageiros} passageiros - Velocidade Máxima: {self.velocidade_maxima} km/h - Tipo de Terreno: {self.tipo_terreno}"

class Automovel(Terrestre):
    def __init__(self, capacidade_passageiros, velocidade_maxima, tipo_terreno, tipo_combustivel):
        super().__init__(capacidade_passageiros, velocidade_maxima, tipo_terreno)
        self.tipo_combustivel = tipo_combustivel
    
    def __str__(self):
        return f"Automóvel - Capacidade: {self.capacidade_passageiros} passageiros - Velocidade Máxima: {self.velocidade_maxima} km/h - Tipo de Terreno: {self.tipo_terreno} - Tipo de Combustível: {self.tipo_combustivel}"
