# List Comprehension
# É uma forma rápida de criar lista a partir de iteráveis
print(list(range(10)))
print()



lista = []
for numero in range(10):
    lista.append(numero)
print(lista, '\n')




lista = [
    numero * 2 #No início colocamos à esquerda do for o que quero que seja iincluído
    for numero in range(10) 
]
# Usando list comprehension
print(lista)
