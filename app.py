from modelos.restaurante import Restaurante
from modelos.avaliacao import Avaliacao

restaurante = Restaurante("McDonald's", "Fast Food")
restaurante2 = Restaurante("Pizza Hut", "Pizzaria")
restaurante3 = Restaurante("Guacamole", "Mexicana")

restaurante2.alternar_status()
restaurante.adicionar_avaliacao("Rodrigo", 5)
restaurante.adicionar_avaliacao("Clara", 3)
restaurante2.adicionar_avaliacao("João", 4)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()


