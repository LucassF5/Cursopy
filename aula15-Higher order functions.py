"""
Higher order functions
Funções de primeira classe
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'
#Função que apresenta uma saudação

def executa(funcao,*args):
    return funcao(*args)
#Função que executa (serve para fazer aparecer na tela) outras funções

print(
    executa(saudacao, 'Bom dia', 'Lucas')
)
# Os parâmetros são colocar a função executa para que seja apresentada a função que queremos e
# a função saudacao, seguida do que queremos que apareça (*args)

print(
    executa(saudacao, 'Boa noite', 'Lucas')
)