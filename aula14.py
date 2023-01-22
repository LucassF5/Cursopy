"""
*args (empacotamento de desempacotamento) #2
*args --> Para quantidades de argumentos não nomeados
"""
"""
def soma(*args):
    total = 0
    for num in args:
        print(f"Total = {total} + número({num})")
        total += num
    return total
# usando return a função caba recebendo e armazenando algum valor
# print só exibe, não armazena valores

soma(1,2,3,4,5,6)
# Assim empacotando todos os números no *args
# Obs: *args são alocados como tupla mas são simplesmente transformados em lista

"""

def soma2(*args):
    total = 0
    for num in args:
        total += num
    return total

numeros = 1,2,3,4,5,6,7,8,9,10 
# Essa variável recebeu uma tupla
outra_soma = soma2(*numeros) # é necessário empacotar para que seja armazenado
print(outra_soma)
print(numeros) # vai ser exibido apenas a tupla
print(*numeros) # vai exibir os valores de cada um, desempacotando
print(sum(numeros)) # faz a mesma coisa que a função soma2 sendo usada na variável outra_soma





