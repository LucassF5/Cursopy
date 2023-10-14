# class Numeros:
#     def __init__(self, nome, num):
#         self.num = None
#         self.nome = nome

#     @classmethod
#     def inicia_num(cls, nome):
#         return cls(nome, 20)


# l1 = Numeros("Lucas", 10)
# l2 = Numeros.inicia_num('L')
# print(l1.num)
# print(l2.nome, l2.num)

class Pets:
    def __init__(self):
        self.patas = None
        self.nome = None

    @property
    def patas(self):
        print("Entrando na property/GETTER")
        return self._patas

    @patas.setter
    def patas(self, valor):
        print("Entrando no setter")
        self._patas = valor

    @property
    def nome(self):
        print("Entrando na property/GETTER")
        return self._nome

    @nome.setter
    def nome(self, valor):
        print("Entrando no setter")
        self._nome = valor


cachorro = Pets()
print("INSTANCIANDO OBJETO\n")
cachorro.patas = 4
print(cachorro.patas)
print("\nPONTO DE MUDANÇA\n")
cachorro.nome = "Auau"
print(cachorro.nome)
