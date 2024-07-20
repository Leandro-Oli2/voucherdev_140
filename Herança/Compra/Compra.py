class Compra:
    def __init__(self, numero, produto, valor):
        self.numero = numero
        self.produto = produto
        self.valor = valor
        self.valor_total = 0
    
    def calcular_valor_total(self):
        icms = 0.17 * self.valor  # Imposto de 17% do ICMS
        frete = 0.05 * self.valor  # Frete de 5% sobre o valor do produto
        self.valor_total = self.valor + icms + frete
    
    def __str__(self):
        return f"Compra Nº {self.numero} - Produto: {self.produto} - Valor Total: R${self.valor_total:.2f}"
class Avista(Compra):
    def __init__(self, numero, produto, valor, desconto):
        super().__init__(numero, produto, valor)
        self.desconto = desconto
    
    def calcular_valor_total(self):
        super().calcular_valor_total()
        self.valor_total -= self.desconto
    
    def preco_com_desconto(self):
        return self.valor - self.desconto
    
    def __str__(self):
        return f"Compra à Vista Nº {self.numero} - Produto: {self.produto} - Valor Total com Desconto: R${self.valor_total:.2f}"
class Parcelada(Compra):
    def __init__(self, numero, produto, valor, numP):
        super().__init__(numero, produto, valor)
        self.numP = numP
    
    def calcular_valor_total(self):
        super().calcular_valor_total()
    
    def valor_parcela(self):
        return self.valor_total / self.numP
    
    def __str__(self):
        return f"Compra Parcelada Nº {self.numero} - Produto: {self.produto} - Número de Parcelas: {self.numP} - Valor Total: R${self.valor_total:.2f} - Valor da Parcela: R${self.valor_parcela():.2f}"
