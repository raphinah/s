from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('Praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.00, 'Grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
sobremesa_sorvete = Sobremesa('Sorvete de Morango', 9.00, 'morango', 'Grande', 'O melhor sorvete da cidade')
sobremesa_sorvete.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)
restaurante_praca.adicionar_no_cardapio(sobremesa_sorvete)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()
