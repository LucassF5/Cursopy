# count é um iterador sem fim (itertools)
from itertools import count

# Count não para de contar, é como se __next__ fosse sempre ativo

c1 = count(step=8, start=8)
r1 = range(8, 100, 8)

print('c1', hasattr(c1, '__iter__'))  # count é um iterável
print('c1', hasattr(c1, '__next__'))  # count é um iterator
print('r1', hasattr(r1, '__iter__'))  # range é um iterável
print('r1', hasattr(r1, '__next__'))  # range não é um iterator

print('count')
for i in c1:
    if i >= 100:
        break

    print(i)
print()
print('range')
for i in r1:
    print(i)
