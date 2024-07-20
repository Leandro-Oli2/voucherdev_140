class Funcionario:
    def __init__(self, nome, sobrenome, horas_t, valor_h ):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_t = horas_t
        self.valor_h = valor_h

    def nomeCompleto(self):
        print(f"O nome completo do funcionario eh: {self.nome} {self.sobrenome}") 
    def calcSalario(self):
        result = self.horas_t*self.valor_h
        return result
    def incremento(self, adc):
        self.valor_h += adc