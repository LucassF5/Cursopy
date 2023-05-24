"""
Função def - return
"""
"""
def função(var):
    return(var)

variavel = função("Valor que eu quero")
if variavel:
   print(variavel)
else:
    ("Nenhum valor")
"""

def divisao(n1,n2):
    if n1/n2:
        return n1/n2
A = float(input("Primeiro num -> "))
B = float(input("Segundo num -> "))
div = divisao(A, B)
if div:
    print(div)
else:
    print("Inválido")
