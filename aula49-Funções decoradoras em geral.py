# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

"""
FUnção decoradora é uma função em que seu trabalho é RECEBER UMA FUNÇÃO, criar outra função
Em que esta(interna) não será executada, apena retornadam sem execução, fazendo uma Closure
Para que a pessoa que está utilizando essa função possa usar a decoradora e enfim utilizar a função decorada
Podendo adicionar coisas antes ou depois do resultado da função, na decoradora
"""

# Essa é a função decoradora


def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)
