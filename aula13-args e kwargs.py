"""
Função def - *args e **kwargs
args = argumentos
kwargs = key-words args (palavra-chave)
"""
# A partir da primeira variável com valor definido as outras posteriores precisarão ser definidas
"""
def func(*args):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))

func(1, 2, 3, 4, 5)
"""
"""
# Transformando as tuplas de args para uma lista; assim posso alterar valores na função
def func(*args):
    args = list(args)
    print(args)
    args[0] = 20
    print(args)

func(1, 2, 3, 4, 5)
"""
"""
# Para ver os valores de cada elemento dos argumentos
def func(*args):
    for v in args:
        print(v)

func(1, 2, 3, 4, 5)
"""
"""
# Desempacotando elementos de uma lista
def func(*args):
    print(args)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(lista)
# Assim fará ums tupla com os elementos da lista e algum elemento que eu colocar na função = ([1, 2, 3, 4, 5],)
func(*lista)
# Desempacotando os elementos para cada posição da tupla = (1, 2, 3, 4, 5)
func(*lista, "elemento 1", "elemento 2")
# Adicionando elementos posteriores à formação da tupla somando-os nela = (1, 2, 3, 4, 5, 'elemento 1', 'elemento 2')
func(*lista, *lista2)
# Desempacotando e somando duas listas
"""
"""
# Desempacotando elementos de uma lista
def func(*args, **kwargs):
    print(args)
    print(kwargs)

lista = [1, 2, 3, 4, 5]
func(*lista, nome="LUCAS", sobrenome="F")
func(f"{[*lista]} é um exemplo de args")
func(nome="LUCAS", sobrenome="F"" é um exemplo de kwargs")
# Somando args e kwargs
# Cada argumento nomeado só será possível acessar usando kwargs
"""
"""
def func(**kwargs):
    print(kwargs['nome'], kwargs['sobrenome'])

func(nome="LUCAS", sobrenome="F")
func(nome="LUCAS", sobrenome="F"" é um exemplo de kwargs")
"""
"""
def func(**kwargs):
    saber = kwargs.get('nome')
    saber2 = kwargs.get('idade')
    # Usar kwargs.get("nome da chave") para saber se esta chave está presente
    print(kwargs['nome'], kwargs['sobrenome'])
    print(saber)
    print(saber2)

func(nome="Lucas", sobrenome="F")
"""

def func(**kwargs):
    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print("Idade não existe")
# Conferindo se uma chave existe, caso sim = ela aparece na tela, caso não = mostra uma mensagem avisando

func(nome="Lucas", sobrenome="F")
func(nome="Lucas", sobrenome="F", idade="X")
