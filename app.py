from modelos.restaurante import Restaurante

# Criando instâncias no app principal
restaurante_cafe = Restaurante('café Da Esquina', 'Cafeteria')
restaurante_cafe.alternar_estado()

restaurante_cafe.receber_avaliacao('Raphael', 9)
restaurante_cafe.receber_avaliacao('Mãe', 7)
restaurante_cafe.receber_avaliacao('Raphael', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()
