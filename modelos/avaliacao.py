
from modelos import restaurante


class Avaliacao:
    def __init__(self, cliente,nota):   
        self._nota = nota
        self._cliente = cliente