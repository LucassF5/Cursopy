# https://stackoverflow.com/questions/2386714/why-is-import-bad

"""
from sys import path  # Importante importar sys

import aula45_package.modulo
from aula45_package import modulo
from aula45_package.modulo import *  # Má prática

# * significa "All", vai importar tudo do módulo

# from aula45_package.modulo import soma_do_modulo
# Assim posso importar a função do package

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
print(aula45_package.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(variavel)
print(nova_variavel)
"""

from aula45_package.modulo import fala_oi

# O Python não consegue ter acesso a coisas de um módulo diferente do que foi importado
# A não ser que seja importado do nome_do_package.nome_package

print(__name__)
# imprimindo __name__ vai dizer se está na main//principal deste arquivo
