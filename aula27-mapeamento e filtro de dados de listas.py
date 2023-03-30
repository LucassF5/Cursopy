# Mapeamento vem à esquerda do for
# Filtro vem à direita do for

# Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'produto1', 'preco': 20},
    {'nome': 'produto2', 'preco': 10},
    {'nome': 'produto3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*produtos, sep="\n")
print("\n\n")
print(*novos_produtos, sep="\n")
print("\n\n")

# Filtro é diferente de map,
# com a condição após o for em list comprehension
# vou SELECIONAR o que eu quero
print()
# Usando filtro

lista = [n for n in range(10) if n < 5]
print(lista)

import pprint

def p(v):
    pprint.pprint(novos_produtos, sort_dicts = False, width = 40)

print("Apresentando uma lista com pprint:")
pprint.pprint(novos_produtos)
print()

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] * 1.05) > 1
]
p(novos_produtos)
