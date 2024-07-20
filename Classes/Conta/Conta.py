class Conta:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        if(self.saldo > 0):
            self.saldo += valor
    def sacar(self, valor):
        if(self.saldo >= valor):
            self.saldo -= valor
        else:
            print("Saldo negativo!!!!")
    def imprimiSaldo(self):
        print(f"O saldo no momento eh: {self.saldo}")