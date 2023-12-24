# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    # Não é uma classe abstrata pois não possui métodos abstratos
    def __init__(self, name):
        self._name = None
        self.name = name

    @property #Getter
    def name(self):
        return ("Este é o getter da classe abstrata", self._name)

    @name.setter #Setter
    @abstractmethod
    def name(self, name): ...
        # return ("Este é o setter da classe abstrata", self._name)


class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        # print('Sou inútil')

    @AbstractFoo.name.setter
    # @property
    def name(self, name):
        self._name = name


foo = Foo('Bar')
print(foo.name) # type: ignore
