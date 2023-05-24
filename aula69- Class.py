# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# print(isinstance(string, str))

"""
Classe é um molde que gera novas instâncias
"""


class Pessoa:  # Criando classe
    ...


p1 = Pessoa()
# Ao atribuir nova variável é criada uma nova instância da classe, novo objeto
p1.nome = 'Lucas'  # type: ignore
p1.sobrenome = 'Franco'  # type: ignore

p2 = Pessoa()
p2.nome = 'Maria'  # type: ignore
p2.sobrenome = 'Sousa'  # type: ignore


print(p1.nome)  # type: ignore
print(p1.sobrenome)  # type: ignore

print(p2.nome)  # type: ignore
print(p2.sobrenome)  # type: ignore
