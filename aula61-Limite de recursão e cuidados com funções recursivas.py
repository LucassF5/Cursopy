# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
# import sys

# sys.setrecursionlimit(1004)
# Definir limite de recursãpo como o valor que for definido


# def recursiva(inicio=0, fim=4):

#     print(inicio, fim)

#     # Caso base
#     if inicio >= fim:
#         return fim

#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio, fim)


# print(recursiva(0, 1001))

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
# Recursão pois no return ele precisa que novamente volte na função para ser executada uma tarefa

# O limite de recursão é em torno de 996, acima disso dá problema de Stack Overflow


print(factorial(5))
print(factorial(10))
print(factorial(100))
