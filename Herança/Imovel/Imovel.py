class Imovel:
    def __init__(self, inscricaoM, valor_aluguel, iptu):
        self.inscricaoM = inscricaoM
        self.valor_aluguel = valor_aluguel
        self.iptu = iptu
    
    def obter_parcela_IPTU(self):
        return self.iptu / 12  
    
    def set_valor_aluguel(self, novo_valor):
        self.valor_aluguel = novo_valor

class Casa(Imovel):
    def __init__(self, inscricaoM, valor_aluguel, iptu, quartos, piscina, area):
        super().__init__(inscricaoM, valor_aluguel, iptu)
        self.quartos = quartos
        self.piscina = piscina
        self.area = area

class Condominio(Imovel):
    def __init__(self, inscricaoM, valor_aluguel, iptu, elevador, area_de_lazer):
        super().__init__(inscricaoM, valor_aluguel, iptu)
        self.elevador = elevador
        self.area_de_lazer = area_de_lazer

class Apartamento(Imovel):
    def __init__(self, inscricaoM, valor_aluguel, iptu, elevador, quartos):
        super().__init__(inscricaoM, valor_aluguel, iptu)
        self.elevador = elevador
        self.quartos = quartos

class Terreno(Imovel):
    def __init__(self, inscricaoM, valor_aluguel, iptu, area):
        super().__init__(inscricaoM, valor_aluguel, iptu)
        self.area = area

class Chacara(Imovel):
    def __init__(self, inscricaoM, valor_aluguel, iptu, area, churrasqueira):
        super().__init__(inscricaoM, valor_aluguel, iptu)
        self.area = area
        self.churrasqueira = churrasqueira

