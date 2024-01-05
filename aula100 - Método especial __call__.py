# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".

from typing import Any


class MyCall:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        # O método __call__ pode receber parâmetros
        # Ele é executado quando a classe é chamada
        # como uma função
        print(f"{nome} está chamando {self.phone}")


class MyClass:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(f"\n{self.phone}\né o funk do {nome} \nque vai dar playstation 2")
        return nome


# inst = classe()
call = MyCall(123456789)
instancia = MyClass("4002-8922")

call("Lucas")
# instancia("Yudi")

retornoClasse = instancia("Yudi")
print("\n",retornoClasse)
#O método __call__ atua na instância e não na classe