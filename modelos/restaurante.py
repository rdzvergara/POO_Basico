from modelos.avaliacao import Avaliacao

class Restaurante:    
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)   

    def __str__(self):
        return f"{self._nome.ljust(25)} | {self._categoria.ljust(25)} | {str(self.media_avaliacao()).ljust(10)} | {self.ativo.ljust(10)}"
    
    @classmethod
    def listar_restaurantes(cls):
        print('Nome do Restaurante'.ljust(25) + ' | ' + 'Categoria'.ljust(25) + ' | ' + 'Avaliação'.ljust(10) + ' | ' + 'Status'.ljust(10))
        for restaurante in cls.restaurantes:
            if restaurante._categoria == "Fast Food".upper(): 
                restaurante._ativo = True
            print(restaurante)

    @property
    def ativo(self):
        return "✔️" if self._ativo else "❌"  
    
    def alternar_status(self):
        self._ativo = not self._ativo

    def adicionar_avaliacao(self, cliente, nota):
        if nota < 0 or nota > 5:
            print("Avaliação inválida. Por favor, insira uma nota entre 0 e 5.")
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        total = sum(av._nota for av in self._avaliacao)
        media = round(total / len(self._avaliacao), 1)
        return media
