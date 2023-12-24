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

#---------------------------------------------------------------
# print("--------------------------------------------\n")


# class Pets:
#     def __init__(self):
#         self.patas = None
#         self.nome = None

#     @property
#     def patas(self):
#         print("Entrando na property/GETTER")
#         return self._patas

#     @patas.setter
#     def patas(self, valor):
#         print("Entrando no setter")
#         self._patas = valor

#     @property
#     def nome(self):
#         print("Entrando na property/GETTER")
#         return self._nome

#     @nome.setter
#     def nome(self, valor):
#         print("Entrando no setter")
#         self._nome = valor


# cachorro = Pets()
# print("INSTANCIANDO OBJETO\n")
# cachorro.patas = 4
# print(cachorro.patas)
# print("\nPONTO DE MUDANÇA\n")
# cachorro.nome = "Auau"
# print(cachorro.nome)
# #---------------------------------------------------------------
print("--------------------------------------------\n")

class Dog:

    #Atributo de classe -> todas vão ter
    species = "Canis familiaris" 

    def __init__(self, name, age):
        #Atributo de instância -> vai variar para cada instância
        self.name = name
        self.age = age

    #Um método de instância que imprime uma frase quando usar o print
    def __str__(self):
        return f"{self.name} é um tioro de {self.age} anos de idade"

#Instanciando a classe
tioro = Dog("Beethoven", 3)
print("->",tioro.name, "\n->",tioro.age)
print(tioro)