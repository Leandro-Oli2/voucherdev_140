class Biblioteca:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
    def alterar_edit(self, e):
        self.editora = e
    def qtd_pag(self):
        print(f"A quantidade de paginas eh: {self.paginas}")
