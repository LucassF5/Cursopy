import copy

from aula46ativ import produtos  # Usando por meio de __init__

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

"""
Primeira resposta
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
"""

novos_produtos = [
    {**p, 'preco': round(p['preco']*1.10, 2)}
    for p in copy.deepcopy(produtos)
]


print("De produtos", *produtos, sep="\n")
print("\n")

print("De novos_produtos", *novos_produtos, sep="\n")
print("\n")
# ------------------------------------------

"""
Segunda resposta
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""
# produtos_ordenados_por_nome = copy.deepcopy(produtos)
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'],
    reverse=True)


def exibir(lista):
    for item in lista:
        print(item)
    print()


print("Ordenados por nome decrescente")
exibir(produtos_ordenados_por_nome)
# ------------------------------------------

"""
Terceira resposta
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""

produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco = sorted(
    produtos,
    key=lambda produto: produto['preco'])


print("Ordenados por preço")
exibir(produtos_ordenados_por_preco)
