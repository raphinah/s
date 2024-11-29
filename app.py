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
restaurante_pizza.receber_avaliacao('Ana', 9)
restaurante_pizza.receber_avaliacao('Carlos', 8)
restaurante_pizza.receber_avaliacao('Marcos', 10)
restaurante_pizza.receber_avaliacao('Joana', 7)
restaurante_pizza.receber_avaliacao('Fernanda', 8)

# Avaliações para Verde Vida
restaurante_veggie.receber_avaliacao('Bruna', 10)
restaurante_veggie.receber_avaliacao('Pedro', 9)
restaurante_veggie.receber_avaliacao('Lucas', 8)
restaurante_veggie.receber_avaliacao('Clara', 10)
restaurante_veggie.receber_avaliacao('Mateus', 9)

# Avaliações para Mar Azul
restaurante_peixe.receber_avaliacao('Marina', 8)
restaurante_peixe.receber_avaliacao('João', 7)
restaurante_peixe.receber_avaliacao('Sophia', 9)
restaurante_peixe.receber_avaliacao('Diego', 6)
restaurante_peixe.receber_avaliacao('Juliana', 8)

# Avaliações para Fiesta Mexicana
restaurante_mexicano.receber_avaliacao('Luís', 6)
restaurante_mexicano.receber_avaliacao('Carla', 9)
restaurante_mexicano.receber_avaliacao('Gabriel', 8)
restaurante_mexicano.receber_avaliacao('Tânia', 7)
restaurante_mexicano.receber_avaliacao('Rodrigo', 10)

# Avaliações para Le Gourmet
restaurante_frances.receber_avaliacao('Renata', 10)
restaurante_frances.receber_avaliacao('Gustavo', 9)
restaurante_frances.receber_avaliacao('Isabela', 10)
restaurante_frances.receber_avaliacao('Arthur', 8)
restaurante_frances.receber_avaliacao('Beatriz', 9)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
