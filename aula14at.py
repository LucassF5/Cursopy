"""
#Questão 1 - Função que multiplica todos os números recebidos e reetorna o total para uma variável
def soma(*args):
    total=1
    for num in args:
        total *= num
    return total

numeros = 1,2,3,65,10,23,77
result = soma(*numeros)
print(result)
print(1*2*3*65*10*23*77)
"""
"""
#Questão 2 - Função que retorna se o num é par ou ímpar
def parimpar(num):
    if num %2 == 0:
        print("par")
        return("par")
    else:
        print("ímpar")
        return("ímpar")



for n in range(5):
    num = int(input("Digite um número: "))
    parimpar(num)
"""

