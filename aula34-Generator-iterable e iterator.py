import sys

# Generator expression, Iterables e Iterators em Python
# Generator é basicamente uma função que 'pausa', utilizado no iterator

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
lista = [n for n in range(1000000)]
# Uma lista grande ocupa bastante espaço de dados na memória
generator = (n for n in range(1000000))
# Um generator vai ocupar menos dados para a mesma lista, usando essa com ()
# Generator, por não guardar na memória, não torna possível saber tamanho, pedir índice ou posição, pois ele só
# entrega um item por vez

print(sys.getsizeof(lista)) 
print(sys.getsizeof(generator))
# .getsizeof mostra o tamanho em bytes que tal coisa está ocupando na memória

print(generator)

# for n in generator: #pode usar essa função pra ver os números presentes na lista do generator
#     print(n)

"""
Diferença entre iterator e generator
Iterator ==> trabalha com iterável, classe que tem os métodos iter e next >>> iterar sobre coisas
Genetator ==> função que pausa >>> Gerar coisas e pausar a cada execução
"""
