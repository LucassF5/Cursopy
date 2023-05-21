# Exercício - Adiando execução de funções
"""
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, *args):
    return funcao(*args)


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)
"""
# ---------------------------

# Resposta

# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y): #Passo1
        return funcao(x, y) #Passo3
    return interna #Passo2

# Para adiar a função basta fazer um closure
# Criar a função em que esta leve a outra a ser executada como parâmetro, e que nesta possua uma interna #Passo1
# Fora da interna vai haver o retorno desta, mas sem executá-la #Passo2
# Agora dentro da interna vai haver a execução da função que queremos #Passo3


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))