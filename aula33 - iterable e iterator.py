# Iterável e Iterator
# Iterável tem a responsabilidade de deter os valores
# Iterator, única responsabilidade é entregar umm valor por vez, saber qual é o PRÓXIMO valor

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

print(next(iterator)) # Aqui vai mostrar o primeiro valor de iterator
print(next(iterator)) # Aqui já vai pular para o próximo
print(next(iterator)) # E assim chega no último
# print(next(iterator)) Como já se encerraram os valores, vai ficar parado no útimo

