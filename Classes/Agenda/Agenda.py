class Agenda:
    def __init__(self, dia, mes, ano, anot = ""):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anot = anot
    def validar(self):
        if(self.dia > 0 and self.dia < 33):
            if(self.mes > 0 and self.mes < 13):
                if(self.ano > 0):
                    print("Data Valida!")
        else:
            print("Data Invalida!")
    def anotar_taf(self, a):
        self.anot = a
    def mostrarAnot(self):
        print(f"A nova  anotacao foi: {self.anot}")
