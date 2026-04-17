from modelos.livro import Livro

livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)   
livro3 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1954)
livro4 = Livro("Jantar Secreto", "Raphael Montes", 2000)

livro3.emprestar_livro()
livro3.emprestar_livro()

Livro.verificar_disponibilidade(1954)

print(livro1)
print(livro2)
print(livro3)
print(livro4)
