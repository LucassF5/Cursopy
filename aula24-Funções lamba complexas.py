"""
LAMBDA NÃO É USADO PARA EXPRESSÕES DIFÍCEIS E EXTENSAS
APENAS PARA SIMPLIFICAR
EXPRESSÕES RÁPIDAS E FÁCEIS
"""

def executa(funcao, *args):
    return funcao(*args)
# Função para exibir


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = executa(
    lambda m: lambda n: n * m,
    2
    # Passa um/os parâmetros por meio de vírgula após a função lambda
)

print(duplica(2))

"""
Não usar assim, pois fica difícil para a compreensão 
"""


print(
    executa(
        lambda x, y: x + y,
        2, 3
    )  
)

""" 
Assim pode,, bem mellhor pra ler e entender
"""

print(
    executa(
        lambda *args: sum(args),
        2, 3
    )  
)



