class Aluno: 
    def __init__(self, nome, ra, n1, n2, n3, n4):
        self.nome = nome
        self.ra = ra
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.media = (n1+n2+n3)/3
    def situation(self):
        if(self.media >= 7.0):
            print(f"Aluno Aprovado!!, pois sua media foi {self.media}")
        elif(self.media < 7.0 and self.media >= 5.0):
            print(f"Aluno de Exame!, pois sua media foi {self.media}")
        else:
            print(f"Aluno Reprovado!, pois sua media foi {self.media}")
        