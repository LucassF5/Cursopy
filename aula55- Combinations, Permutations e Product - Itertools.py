# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos
from itertools import combinations, permutations, product

# A maioria retorna um iterator


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    # Usando * para expandir a lista, e sep para melhor visualização
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2))
# COmbinations não exibe os dados com repetição
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
