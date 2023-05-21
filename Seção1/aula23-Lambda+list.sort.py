# Função lambda em Python
# Funções anônimas que contém apenas uma linha
# Tudo deve ser contido em apenas uma única expressão

# lista.sort() --> ordena uma lista, função de lista
# sorted(lista) função que cria uma nova lista ordenada mas com uma cópia rasa da lista original

"""
Como utilizar expressões lambda

variável = lambda parâmetro(s): função_a_ser_usada/expressão,
           Valores/expressões para os parâmetros

expressão = lambda x, y: x + y
print(expressão(8,3))

"""

lista1 = [3,35,2,5,8,9,0,1]
lista1.sort() # se usar reverse = True também funciona
print(lista1)

lista1 = [3,35,2,5,8,9,0,1]
lista2 = sorted(lista1)
print(lista2)

print()

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome'] # vai ordenar por nome
#     return item['sobrenome'] # vai ordenar pelo sobrenome

# lista.sort(key=ordena)

#Usando a função lambda
# lista.sort(key=lambda item:item['nome'])
# A função lamba definiu item como parâmetro e ordenou pelo segundo parâmetro que foi nome

# for item in lista:
#     print(item)
#     print()

# -------------------------------------------

# Agora usando a função sorted

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key = lambda item:item['nome'])
l2 = sorted(lista, key = lambda item:item['sobrenome'])

exibir(l1)
exibir(l2)
