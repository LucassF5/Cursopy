# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))
# Toda função generator usa yield

"""
def generator(n=0):
    yield 1 #pausar
    # usar a função next mais uma vez, mesmo com o generator, abre-se  uma exceção e apresenta o próximo

    print("Continuando...")
    yield 2 #pausar

    print("Mais uma vez...")
    yield 3 #pausar

    print('Vou terminar') #Abre uma exceção a partir daqui
    # Usa a exceção e executa o próximo comando
    return 'ACABOU'

gen = generator(n-=0)
for n in gen:
    print(n)
"""

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)