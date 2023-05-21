# Variáveis livres + nonlocal (locals, globals)
"""
Variável livre é a que não está definida no escopo da função interna mas faz parte dela
Logo, não pode ser alterada, a menos que seja definida a expressão 'nonlocal' antes dela
"""

# print(globals())
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial  # Iniciando a variável

    def interna(valor_a_concatenar=''):
        # Note que a variável não faz parte do escopo da função interna
        # Definindo a variável como nonlocal para ser possível fazer alterações
        nonlocal valor_final
        valor_final += valor_a_concatenar  # Operação com a variável
        return valor_final
    return interna


c = concatenar('a')  # Definindo o valor da variável
# Logo na chamada da função é necessário colocar um valor para a interna, não esquecer
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)
