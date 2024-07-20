from datetime import datetime
class Notafiscal:
    def __init__(self, numero, tipo, serie, cnpj, razaoS, data, valorP, icms, frete, ipi, valorT=0 ):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razaoS = razaoS
        self.data = data
        self.valorP = valorP
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valorT = valorT
    def obterNum(self, n):
        self.numero = n
    def obterDataE(self):
        d = input("Informe a data de emissao: ")
        try:
            dates = datetime.strftime(d, "%d/%m/%Y")
            print(f"Data de emissao registrada: {dates.strftime('%d/%m/%Y')}")
        except ValueError:
            print("Formato de data invalido!")
        
    def alterarRazao(self, s):
        self.razaoS = s

    def calcT(self):
        self.valorT = self.valorP + self.frete + self.icms + self.ipi
        print(f"O valor total eh: {self.valorT}")
