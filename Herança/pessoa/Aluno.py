from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome, idade, n1, n2, media = 0):
        super().__init__(nome, idade)
        self.__n1 = n1
        self.__n2 = n2
        self.media = media
    def calc_media(self):
        media = (self.__n1+self.__n2)/2
        return media
    def estudar(self):
        print(f"Aluno: {self.nome} esta estudando!")

    