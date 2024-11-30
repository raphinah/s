from modelos.restaurante import Restaurante

# Criando instâncias no app principal
restaurante_cafe = Restaurante('café Da Esquina', 'Cafeteria')
restaurante_cafe.alternar_estado()

restaurante_pizza = Restaurante('Pizza Suprema', 'Pizzaria')

restaurante_veggie = Restaurante('Verde Vida', 'Vegana')
restaurante_veggie.alternar_estado()

restaurante_peixe = Restaurante('Mar Azul', 'Frutos do Mar')
restaurante_peixe.alternar_estado()

restaurante_mexicano = Restaurante('Fiesta Mexicana', 'Mexicana')

restaurante_frances = Restaurante('Le Gourmet', 'Francesa')
restaurante_frances.alternar_estado()

# Avaliações para Café Da Esquina
restaurante_cafe.receber_avaliacao('Raphael', 10)
restaurante_cafe.receber_avaliacao('Charlie', 7)
restaurante_cafe.receber_avaliacao('Max', 5)
restaurante_cafe.receber_avaliacao('Benji', 9)
restaurante_cafe.receber_avaliacao('Tu', 2)

# Avaliações para Pizza Suprema


# Avaliações para Verde Vida
restaurante_veggie.receber_avaliacao('Bruna', 10)
restaurante_veggie.receber_avaliacao('Pedro', 9)
restaurante_veggie.receber_avaliacao('Lucas', 8)
restaurante_veggie.receber_avaliacao('Clara', 10)
restaurante_veggie.receber_avaliacao('Mateus', 9)

# Avaliações para Mar Azul
restaurante_peixe.receber_avaliacao('Marina', 4)
restaurante_peixe.receber_avaliacao('João', 0)
restaurante_peixe.receber_avaliacao('Sophia', 1)
restaurante_peixe.receber_avaliacao('Diego', 5)
restaurante_peixe.receber_avaliacao('Juliana', 7)

# Avaliações para Fiesta Mexicana
restaurante_mexicano.receber_avaliacao('Luís', 4)
restaurante_mexicano.receber_avaliacao('Carla', 3)
restaurante_mexicano.receber_avaliacao('Gabriel', 1)
restaurante_mexicano.receber_avaliacao('Tânia', 7)
restaurante_mexicano.receber_avaliacao('Rodrigo', 0)

# Avaliações para Le Gourmet
restaurante_frances.receber_avaliacao('Renata', 0)
restaurante_frances.receber_avaliacao('Gustavo', 9)
restaurante_frances.receber_avaliacao('Isabela', 1)
restaurante_frances.receber_avaliacao('Arthur', 8)
restaurante_frances.receber_avaliacao('Beatriz', 2)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
