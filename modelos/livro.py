
class Livro:
    livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f"{self._titulo} por {self._autor} ({self._ano_publicacao})"
    
    def emprestar_livro(self):
        if self._disponivel:
            self._disponivel = False
            print(f"Você emprestou '{self._titulo}'.")
        else:
            print(f"Desculpe, '{self._titulo}' não está disponível no momento.")

    @classmethod
    def verificar_disponibilidade(cls, ano): 
        print("Livros disponiveis de " + str(ano) + ":")     
        for livro in cls.livros:
            if livro._ano_publicacao == ano and livro._disponivel:
                print(livro)