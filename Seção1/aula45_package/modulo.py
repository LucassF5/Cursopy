# __all__ = [
#     'variavel',
#     'soma_do_modulo',
#     'nova_variavel',
# ]
# __all__ é usado para colocar o que eu permito que seja importado se for usado *
# Caso deixe de colocar o nome de função ou variável, essa não vai estar disponível

from aula45_package.modulo_b import fala_oi

# usar o from com o nome_package.nome_arquivo para importar a função

variavel = 'Alguma coisa'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'OK'

fala_oi()
