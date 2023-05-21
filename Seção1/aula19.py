# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Franco1',
    'sobrenome': 'Franco' # Quando há duas chaves iguais, só irar atualizar o valor e permanecer uma única key
}

# Importante lembrar de colocar () após usar os métodos de dicionários
print("Método len")
print(pessoa.__len__()) # Retorna a quantidade de chaves no dicionário, desconsiderando as repetidas
print(len(pessoa),"\n") # Outra forma de usar len

print("Método keys")
print(pessoa.keys()) # Repassa as chaves
print(list(pessoa.keys()),"\n") # Para ficar mais bonito e legível, convém transformar em lista ou tupla

print("Método values")
print(tuple(pessoa.values()),"\n") # Repassa os valores contidos nas chaves

print("Método items")
print(list(pessoa.items()),"\n") # Apresenta chave e valor

print("Método setdefault")
pessoa.setdefault('idade', 20) # Caso não tenha a variável no dicionário, ele introduz e com um valor base
print(pessoa['idade'],"\n")

print("Método get")
print(f"A chave 'altura' {pessoa.get('altura', 'não existe')}","\n") 
# obtém uma chave, caso ela náo exista retorna "None", indicando que não exista, ou pode-se passar um valor padrão

pessoa["altura"] = 'X' # adicionando chave e valor no dicionário

print("Método pop")
pessoa.pop('sobrenome') # pop apaga o item nomeado
print(pessoa,"\n")

print("Método popitem")
ultima_chave = pessoa.popitem() 
# No método "popitem" é excluída a última chave do dicionário
# Não pode-se passar a chave dentro dos parêntesis
print(f'Chave a ser excluída {ultima_chave}')
print(pessoa,"\n")

print("Método update")
pessoa.update({
    'idade' : '22', # O método update tanto pode atualizar uma chave do dicionário
    'Sobrenome' : 'Franco', # Quanto pode criar uma nova chave para esse mesmo
    "last_nome" : "Rocha" 
})
print(pessoa)

# Outras formas de utilizar o método update
# pessoa.update(nome = "LUCAS", idade = 21)
# tupla = (('nome',"Lucas") , ("idade", 22))
# lista = [["Nome", 'Lucas'], ['idade', 21]]

for chave in pessoa:
    print("\n",chave, pessoa[chave])