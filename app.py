from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_cofee = Restaurante('Cofee and milk', 'Cafeteria e restaurante')
prato_bolacha = Prato('Bolacha', 1.00, 'A melhor bolachinha')
bebida_cafe = Bebida('Café com leite', 7.00, 'Uma dilícia')
restaurante_cofee.adicionar_no_cardapio(prato_bolacha)
restaurante_cofee.adicionar_no_cardapio(bebida_cafe)

def main():
    restaurante_cofee.exibir_cardapio

if __name__ == '__main__':
    main()
