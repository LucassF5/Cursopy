"""
Entrada de dados - INPUT
Input, serve para fazer o usuário digitar uma informação
"""
nome = input("Qual o seu nome?: ")
idade = input("Qual sua idade? ")
# Input sempre vai retornar uma string
# Para solucionarmos o problema alteramos o tipo com um Cast
ano_nasc = 2020-int(idade)
print(f'\nO usuário digitou {nome}, e o tipo da variável é '
      f'{type(nome)}\n')
print(f"{nome} tem {idade} anos.\n")

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite um segundo número: "))
print("\n", num_1 + num_2)
print("\n", num_1 - num_2)
print("\n", num_1 ** num_2)

"""
IF, ELIF (else if), ELSE
ELIF e ELSE atuam em conjunto e somente na presença de um operador if
Todos precisam manter uma mesma linha de identação para fazer parte do conjunto, senão serão de outro
Para o operador funcionar é imprescindível o uso dos :(dois pontos)
A indentação se faz com um número aconselhável de 4 espaços
# É possível ter variáveis e operações dentro dos operadores
"""
if True:
    print("Primeiro exemplo verdadeiro")
    nome = input("Qual seu nome?: ")
    print(f"Seu nome é {nome}")
# É fundamental o espaço na linha logo após
elif True:
    print("Segundo exemplo")
# Elif surge como um escape caso o if possua mais de uma sentença que possa ser utilizado
# If e Elif, respectivamente, são lidos juntos, o que estiver verdadeiro primeiro prevalece
# É possível a utilização de mais de um elif, se necessário
else:
    print("Terceiro exemplo")
# Else vem como o contrário de if, sendo usado como "se não"
"""
Operadores relacionais
== igualdade
> maior que
>= maior igual
< menor que
<= menor igual
!= diferente
"""

nome = input("Qual seu nome")
idade = int(input("Qual sua idade"))
idade_menor = 18
idade_maior = 30
# Suposição sobre um empréstimo
if idade_menor < idade < idade_maior:
    print(f"{nome} pode pegar o empréstimo")
else:
    print(f"{nome} não pode pegar empréstimo")
