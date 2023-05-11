# groupby - agrupando valores (itertools)
from itertools import groupby

# groupby vai precisar que seja informado por qual chave do dict precisa ser ordenado

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos_ordenados = sorted(alunos, key=lambda aluno: aluno['nota'])
# Ordenando(sorted) a lista(alunos), em que a key lambda seleciona aluno,
# e essa vai ordenar pelo nome key=lambda aluno: aluno['nota']
# for aluno in alunos_ordenados:  # imprimindo a lista de alunos ordenados por nome
#     print(aluno)


def ordena(aluno):  # Criando a ordem de ordenação do código
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

# Relembrando .sort e sorted
# def ordena(list):
#     for item in list:
#         print(item)


# alunos = ['a', 'a', 'c', 'a', 'b', 'c', 'c', 'b']
# print(alunos, "1 vez\n")  # Desordenado
# alunos.sort()
# print(alunos, "2 vez\n")  # Ordenado
# ordena(sorted(alunos))  # Vai imprimir ordenado
