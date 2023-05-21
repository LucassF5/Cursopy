print("Sem list comprehension")
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))
print(lista)
print()
print("Com list comprehension mas desordenado")
lista = [
    x
    for x in range(3)
    for y in range(3)
]
print(lista)
print()
print("Com list comprehension e ordenado")
lista = [
    (x, y)  #Isso que vai ser adicionado na lista
    for x in range(3)
    for y in range(3)
]
print(lista)
