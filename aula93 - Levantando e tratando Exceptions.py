# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    #Criando exception
    ...


class OutroError(Exception):
    ...


def levantar():
    #Levantando exception
    exception_ = MeuError('a', 'b', 'c')
    exception_.add_note("Adicionando comentário na exception")
    exception_.add_note("Aparece no traceback")
    raise exception_


try:
    #Tratando exception
    levantar()
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__) #Pegando o nome da exception que lançou a exception
    print(error.args) #Pegando os argumentos da exception
    print()
    exception_ = OutroError('Vou lançar de novo')
    raise exception_ from error #Relançando exception