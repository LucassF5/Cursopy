"""
Split, Join, enumerate em Python
Split = Dividir uma lista # str ¬  significa dividir
Join - Juntar uma lista #str
Enumerate - enumerar elementos da lista # list / objetos iteráveis
Desempacotamento de listas
"""

string = "O Brasil é o país do futebol, o Brasil é penta, Brasil"
lista = string.split(" ")
lista2 = string.split(",")
# em split(""), o símbolo colocado vai representar o lugar que haverá divisão
# o primeiro foi separando onde havia espaços, no segundo o critério de separação foi onde havia vírgula
# print(lista2)
"""
for valor in lista:
    print(valor)
print()
for valor in lista2:
    print(valor)
"""
palavra = ""
cont = 0
for valor in lista:
    """
    print(f' A palavra {valor} apareceu {lista.count(valor)}x vezes na frase.\n')
print("\n\n")
"""
    qtd_vezes = lista.count(valor)

    if qtd_vezes > cont:
        cont = qtd_vezes
        palavra = valor
print(f'A palavra que apareceu mais vezes foi {palavra}, apareceu ({cont}x)')

# A função '.strip' remove espaços (desnecessários) do início e fim
for valor in lista2:
    print(valor.strip().capitalize())
# A função.capitalize deixa a primeira letra maiúscula
# A função split divide uma string gerando uma lista dependendo de como ordenamos para separar
"""
Join serve para juntar os elementos de uma lista e transformar em uma string
"""
str = "O Brasil é penta campeão"
list = str.split(" ")
str2 = '*'.join(list)
# A função.join precisa que seja explicitado o elemento que vai fazer a divisão dos elementos da lista
# No caso vai ser a vírgula, e dentro do (), parêntesis, adicionar o local do qual é para pegar os valores
print(str)
print(list)
print(str2)

"""
Desempacotamento de listas
"""
lista = ["Luiz", "João", "Maria", 1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
n1, n2, n3, *outros_valores, ultimo_da_lista = lista
# Ao colocar o * e digitar algo vai ser criada uma variável contendo o resto dos elementos
# Caso seja criada alguma outra, após essa, os últimos valores serão adicionados na ordem em que aparecem
print(*outros_valores)
"""
n1 = índice 0
n2 = índice 1
n3 = índice 2
*outros_valores = Cria uma lista com valores restantes e armazena em outra variável
ultimo_da_lista = último índice (valor 100)
"""
