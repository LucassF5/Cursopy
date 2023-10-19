# super() e a sobreposição de membros - Python Orientado a Objetos
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):  # SOBREPONDO MÉTODO UPPER DE STR
#         print("CHAMANDO MÉTODO UPPER")
#         return super().upper()  # RETORNANDO CÓDIGO DO MÉTODO PAI MAS AINDA COM MINHAS ALTERAÇÕES


# string = MinhaString("Lucas")
# print(string.upper()


class A:
    atributo_a = "valor A"

    def __init__(self, atributo):  # Definindo que a classe A necessita receber um atributo
        self.atributo = atributo

    def metodo(self):
        print("A")


class B(A):  # Por ser filha da classe A, então vai precisar setar um atributo na inicialização
    atributo_b = "valor B"

    def __init__(self, atributo, outra_coisa):
        # Chamando o construtor da classe pai e setrando um atributo a ela
        super().__init__(atributo)
        self.outra_coisa = outra_coisa  # Setando um atributo a classe B

    def metodo(self):
        print("B")


class C(B):  # A classer C vai precisar declarar dois atributos na inicialização
    atributo_c = "valor C"

    def __init__(self, *args, **kwargs):
        print("Mostrando algo antes de setar os atributos para as super classes")
        # Setando assim os atributos para as super classes
        super().__init__(*args, **kwargs)

    def metodo(self):
        super(C, self).metodo()
        A.metodo(self)  # Vai chamar o método da classe A
        print("C")


c = C("Atributo", "Segundo atributo")
print(c.atributo)
print(c.outra_coisa)
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()

# print(C.mro())  # method resolution order
# Method resolution order: A classe e todas as super classes de que ele herda
