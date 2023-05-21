"""
# 1 - Função que exibe uma saudação como os parâmetros saudacao e nome;

def func(saudacao, nome):
    print(saudacao, nome)

saudação = func(saudacao = "Olar", nome = input("Seu nome: "))
#-----------------------------------------------------------------------------------------------------------------------
"""
"""

# 2 - Crie uma função que recebe 3 números e exibe a soma entre eles;

def func(n, n1, n2):
    print(n+n2+n1)
    
soma = func(n = int(input("N: ")), n1 = int(input("N: ")), n2 = int(input("N: ")))
#-----------------------------------------------------------------------------------------------------------------------
"""
"""

# 3 - Função que recebe 2 números. O primeiro é um valor e o segundo um percentual.
# Retorne o valor do primeiro somado com do aumento percentual do mesmo;

def porcem(num, porc):
    return num + (num * porc/100)

num = float(input("Digite um número: "))
num2 = float(input("Digite um número: "))
resultado = porcem(num, num2)
print(resultado)
#-----------------------------------------------------------------------------------------------------------------------
"""
"""

# 4 - Fizz Buzz - Se o parâmetro da função for um número divisível por 3, retorne Fizz;
# Se for divisível por 5, retorne Buzz; E se for divisível por 3 e 5, retorne FizzBuzz, caso contrário, retorne o num;

def FizzBuzz(num):
    if num %3 == 0 and num %5 == 0:
        return "FizzBuzz"
    elif num %3 == 0:
        return "Fizz"
    elif num %5 == 0:
        return "Buzz"
    else:
        return num

num = int(input("Digite um número: "))
result = FizzBuzz(num)
print(result)
#-----------------------------------------------------------------------------------------------------------------------
"""
"""
# Teste 1
def func2():
    var1 = "lucas"
    return var1

def func(arg):
    print(arg)

var = func2()
func(var)
#-----------------------------------------------------------------------------------------------------------------------
"""
"""
# Função principal  que retorna duas outras funções com número diferente de argumentos
def func(nome):
    return f"Oi {nome}"

def func1(msg="Oi"):
    return msg

def mestre(funcao,*args, **kwargs):
    return funcao(*args, **kwargs)

exe = mestre(func, nome="Lucas")
print(exe)

exe2 = mestre(func1)
print(exe2)
#-----------------------------------------------------------------------------------------------------------------------
"""
