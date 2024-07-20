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
class Aereo(Transporte):
    def __init__(self, capacidade_passageiros, velocidade_maxima, envergadura):
        super().__init__(capacidade_passageiros, velocidade_maxima)
        self.envergadura = envergadura
    
    def __str__(self):
        return f"Transporte Aéreo - Capacidade: {self.capacidade_passageiros} passageiros - Velocidade Máxima: {self.velocidade_maxima} km/h - Envergadura: {self.envergadura}"


class AviaoMonomotor(Aereo):
    def __init__(self, capacidade_passageiros, velocidade_maxima, envergadura, tipo_motor):
        super().__init__(capacidade_passageiros, velocidade_maxima, envergadura)
        self.tipo_motor = tipo_motor
    
    def __str__(self):
        return f"Avião Monomotor - Capacidade: {self.capacidade_passageiros} passageiros - Velocidade Máxima: {self.velocidade_maxima} km/h - Envergadura: {self.envergadura} - Tipo de Motor: {self.tipo_motor}"


class AviaoComercial(Aereo):
    def __init__(self, capacidade_passageiros, velocidade_maxima, envergadura, numero_assentos):
        super().__init__(capacidade_passageiros, velocidade_maxima, envergadura)
        self.numero_assentos = numero_assentos
    
    def __str__(self):
        return f"Avião Comercial - Capacidade: {self.capacidade_passageiros} passageiros - Velocidade Máxima: {self.velocidade_maxima} km/h - Envergadura: {self.envergadura} - Número de Assentos: {self.numero_assentos}"

class Aquatico(Transporte):
    def __init__(self, capacidade_passageiros, velocidade_maxima, tipo_propulsao):
        super().__init__(capacidade_passageiros, velocidade_maxima)
        self.tipo_propulsao = tipo_propulsao
    
    def __str__(self):
        return f"Transporte Aquático - Capacidade: {self.capacidade_passageiros} passageiros - Velocidade Máxima: {self.velocidade_maxima} km/h - Tipo de Propulsão: {self.tipo_propulsao}"


class Lancha(Aquatico):
    def __init__(self, capacidade_passageiros, velocidade_maxima, tipo_propulsao, comprimento):
        super().__init__(capacidade_passageiros, velocidade_maxima, tipo_propulsao)
        self.comprimento = comprimento
    
    def __str__(self):
        return f"Lancha - Capacidade: {self.capacidade_passageiros} passageiros - Velocidade Máxima: {self.velocidade_maxima} km/h - Tipo de Propulsão: {self.tipo_propulsao} - Comprimento: {self.comprimento} metros"


class Navio(Aquatico):
    def __init__(self, capacidade_passageiros, velocidade_maxima, tipo_propulsao, carga_maxima):
        super().__init__(capacidade_passageiros, velocidade_maxima, tipo_propulsao)
        self.carga_maxima = carga_maxima
    
    def __str__(self):
        return f"Navio - Capacidade: {self.capacidade_passageiros} passageiros - Velocidade Máxima: {self.velocidade_maxima} km/h - Tipo de Propulsão: {self.tipo_propulsao} - Carga Máxima: {self.carga_maxima} toneladas"
