# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(l1, l2)))  # zip pega do menor valor
# zip_longest começa pegando do maior valor, a maior lista
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))

# Para somar/unir valores de duas listas
lista_soma = [x + y for x, y in zip(l1, l2)]
print(lista_soma)

# dict_tudo = {}
# combinado = list(zip(l1, l2))
# print(combinado)

# num_itens = len(l1)
# for i in range(len(l1)):
#     dict_tudo.update({l1[i]: l2[i]})
# print(dict_tudo)

# def zipper(l1, l2):
#     intervalo = min(len(l1), len(l2))
#     return [(l1[i], l2[i]) for i in range(intervalo)]
