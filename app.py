from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

# Criando instâncias no app principal
restaurante_cafe = Restaurante('café Da Esquina', 'Cafeteria')
bebida_coca = Bebida('Coca Cola', 7.00, 'Lata')
prato_batata = Prato('Batata Frita', 9.00, 'pequena')

def main():
    print(bebida_coca)
    print(prato_batata)

if __name__ == '__main__':
    main()
