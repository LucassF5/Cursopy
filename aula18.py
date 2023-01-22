# Manipulando chaves e valores em dicionários
pessoa = {}

# Criando chaves e valor em dicionários
# pessoa['nome'] = "Lucas"
# print(pessoa['nome'])

#Criando chaves dinâmicas
chave = 'nome_completo'

pessoa[chave] = "Lucas"
pessoa['sobrenome'] = 'Franco'
print(pessoa)


print(pessoa[chave],'\n') # Acessando o valor contido na chave do dicionário

#Alterando o valor da chave
pessoa[chave] = "Silvia"

#Deletando o valor da chave
del pessoa['sobrenome']
print(pessoa, '\n')

# Como saber se uma chave existe
print("Se a chave não existir ela retorna:", pessoa.get('sobrenome')) # Caso não exista vai retornar None
if pessoa.get("sobrenome") is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])
