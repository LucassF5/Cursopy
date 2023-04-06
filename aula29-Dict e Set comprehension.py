# Dictionary comprehension e Set comprehension
produto = {
    'nome' : 'Caneta azul',
    'preço': 2.50,
    'categoria': 'Escritório'
}

# for chave, valor in produto.items():
#     print(chave, valor)

dc = {
    chave : valor.upper()
    if isinstance(valor, str) else valor  # isistance serve para saber se determinada coisa é de um certo tipo
    # caso possa ser de mais de um tipo só colocar no ()
    # Ex: isintance(valor, (int, float))
    for chave, valor
    in produto.items()
    if chave == 'categoria' #Assim só incluiria SE E SOMENTE SE essa condição for verdadeira, se for diferente não entra
}

print(dc, "\n")

lista = [
    ('a','valor a'),
    ('b','valor b'),
    ('c','valor c')
]

dc2 = {
    chave : valor
    for chave, valor in lista

}

print(dc2,"\n")

print(dict(lista)) # Um método pra transformar lista, consegur transofrmar listas parecidas com dicionário, que parece chave, valor

"---------------------------------------------------------------------------------------------"

set1 = {i**2 for i in range(10)}
print(set1)

