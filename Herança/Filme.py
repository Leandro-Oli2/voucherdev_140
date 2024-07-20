class Filme:
    def __init__(self, nome, duracao):
        self.__nome = nome
        self.__duracao = duracao

    def play(self):
        print(f"{self.__nome} comecou!!")
    
    def getduracao(self):
        return self.__duracao
    
    def setnome(self, novon):
        self.__nome = novon

    def getnome(self):
        return self.__nome
######
class Drama(Filme):
    def __init__(self, nome, duracao, ator):
        super().__init__(nome, duracao)
        self.ator = ator
filme1 = Drama("slakkk", 177, "Silvester Stallone")
print(filme1.getduracao())
filme1.setnome("Rocky Balboa")
print(filme1.getnome())

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

class Acao(Filme):
    def __init__(self, nome, duracao, ator):
        super().__init__(nome, duracao)
        self.ator = ator
filme2 = Acao("Rambo 4", 187, "Silvester Stallone")
print(filme2.getduracao())
filme2.play()