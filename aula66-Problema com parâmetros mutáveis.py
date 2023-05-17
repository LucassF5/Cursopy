# Problema dos parâmetros mutáveis em funções Python

# NUNVA PASSAR VALOR MUTÁVEL QUANDO FOR PASSAR UM PARÂMETRO
# SEMPRE COLOCAR NONE E CRIAR DENTRO DA FUNÇÃO
def adiciona_clientes(nome, lista=None):
    if lista is None:  # Caso não seja passado nada, então vai ser criado uma lista para determinada ação
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
# Após ser criado pela primeira vez, é necessário passar o parâmetro para que seja imcrementado
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
