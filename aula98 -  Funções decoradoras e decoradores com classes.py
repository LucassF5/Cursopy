# Funções decoradoras e decoradores com classes

def meu_repr(self):
    # Essa função vai ser o repr da classe
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr # Fazendo referência à função meu_repr
    # O repr da classe vai ser a função meu_repr
    # Que vai ser a representação da classe
    return cls

#Utilizando sintax sugar e decoradores
@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

#Utilizando sintax sugar e decoradores
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)