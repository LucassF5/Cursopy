# Métodos de classe + factories (fábricas)
# São métodos onde 'self' será 'cls', ou seja
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe

# P.S: Factory method é um método que cria um objeto com algo arbitrário(que já foi definido previamente)
# criar algo com um método que já define valores para os atributos do objeto

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print("Olá")

    @classmethod
    def criar_com_50_anos(cls, nome):  # vai criar o objeto já com atributo setado
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)

# factory method
# método que cria um objeto com algo arbitrário


p1 = Pessoa('Lucas', 22)
p2 = Pessoa.criar_com_50_anos("Nome da pessoa")
p3 = Pessoa.criar_sem_nome(22)
p4 = Pessoa("Nome2", 54)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)

# Pessoa.metodo_de_classe()
