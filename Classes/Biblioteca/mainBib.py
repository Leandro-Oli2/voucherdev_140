from Biblioteca import Biblioteca

livro = Biblioteca("o Pequeno Principe", "Charles Darwin", "Globo Brasil", 50)
livro.alterar_edit("Sla ")
print(f"A NOVA EDITORA EH {livro.editora}")
livro.qtd_pag()