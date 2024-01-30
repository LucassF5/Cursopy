# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs): # Recebendo argumentos/valores e adiando a função
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(2) # Classe decoradora chamando da função
# É chamada como se fosse uma função @Decoradora()()
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 4) # Passando valores para a instância ativar a decoradora
print(dois_mais_quatro)