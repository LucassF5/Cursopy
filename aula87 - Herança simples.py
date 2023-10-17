# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:  # Criando a classe Pessoa
    cpf = "CPF na classe Pessoa"

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):  # CRIANDO O MÉTODO FALAR NOME CLASSE
        print(self.nome, self.sobrenome,
              " Classe: " + self.__class__.__name__)


class Cliente(Pessoa):  # CRIANDO CLASSE CLIENTE QUE HERDA DE PESSOA
    cpf = "CPF na classe CLIENTE"


class Aluno(Pessoa):  # CRIANDO CLASSE ALUNO QUE HERDA DE PESSOA
    cpf = "CPF na classe Aluno"


print(Pessoa.cpf)

c1 = Cliente("Lucas", "Franco")
c1.falar_nome_classe()
print(c1.cpf)

a1 = Aluno("Maria", "Decina")
a1.falar_nome_classe()
print(a1.cpf)
