"""
a=2
b=3.5
c="isso é uma string"
print(a,b,c)
print(a*c)

d=[1,2,3,4,5]
print(a*d)
"""
"""
j = input("Escreva algo: ")

if j.isnumeric():
        print("É número")

else:
        print("Não é número")
        if j.isdigit():
         print("Você digitou uma letra")
"""
"""
c = 500
t = 10
j = 1.2 * c * t
m = c+j
print(c)
print(t)
print(j)
print(m)
"""
"""
n = int(input("Insira qualquer número: "))
mul = 0
for count in range(2,n):
    if (n%count==0):
        print("Múltiplo de", count)
        mul+=1
if(mul==0):
    print("É primo")
else:
    print("Tem", mul, "múltiplos acima de 2 e abaixo de ", n)
"""
# __________________________________________________________________________________________________________________
"""
# Conversor de medidas
# Pegar um valor em metros e transformar em cm e mm
for i in range(0,5,1):
    medida= float(input("Digite um valor em metros: "))
    km = medida * (10 ** (-3))
    hm = medida * (10 ** (-2))
    cm = medida * 100
    mm = medida * 1000
    print(f'Você digitou {medida} m')
    print(f"Esse valor convertido em hm é {hm:.4f} hm e em km é {km:.4f} km")
    print(f"Esse valor convertido em cm é {cm} cm e em mm é {mm} mm\n")
"""
# __________________________________________________________________________________________________________________
"""
# Tabuada
for i in range(0,3,1):
    n= int(input("Digite um número inteiro: "))
    print("---------")
    print(f"{n} x 1 = {n*1}")
    print(f"{n} x 2 = {n*2}")
    print(f"{n} x 3 = {n*3}")
    print(f"{n} x 4 = {n*4}")
    print(f"{n} x 5 = {n*5}")
    print(f"{n} x 6 = {n*6}")
    print(f"{n} x 7 = {n*7}")
    print(f"{n} x 8 = {n*8}")
    print(f"{n} x 9 = {n*9}")
    print(f"{n} x 10 = {n*10}")
    print("---------")
"""
# __________________________________________________________________________________________________________________
"""
# Conversor de moedas
for i in range(0,3,1):
    din = float(input("How much dinheiros vc tem na carteira?\n -> R$"))
    dol = 3.27
    conv = din/dol
    print(f"Você pode converter {din} para {conv:.2f} dólares")
"""
# __________________________________________________________________________________________________________________
"""
# Tinta para a parede
# Altura - Largura - Área - 1L de tinta pra 2 m de parede
for i in range(0,3,1):
    H = float(input("Altura da parede: "))
    L = float(input("Largura da parede: "))
    area = L * H
    tinta = area/2
    print(f"A {H} vezes {L} resulta em uma área de {area:.2f}m²")
    print("Você precisa de {:.2f} litros de tinta para pintar a parede\n".format(tinta))
"""
# __________________________________________________________________________________________________________________
"""
for i in range(0,3,1):
    prod=float(input("Preço do produto: "))
    prod2 = prod * (5/100)
    prod3 = prod - prod2
    print(prod3)
"""
# __________________________________________________________________________________________________________________
"""
# Reajuste salarial
for i in range(0,3,1):
    sal=float(input("Salário do funcionário: "))
    aum =sal + (sal * (15/100))

    print(f"O salário do funcionário era {sal:.2f}R$, e com 15% de aumento ficou {aum:.2f}R$")
"""
# __________________________________________________________________________________________________________________
"""
# Conversão de temperatura
#  (0 °C × 9/5) + 32 = 32 °F
C = float(input("Entre com a temperatura em Celsius: "))
F = (C * 9/5) +  32
print(f"A temperatura em C é {C:.1f}ºC e em Fahrenheit é {F:.1f}ºF")
"""
# __________________________________________________________________________________________________________________
"""
# Aluguel de carros
# C - 60 por dia // 0,15 por km
Dias = int(input("Quantos dias você passou com o carro: "))
Km = float(input("Quantos km você andou com o carro: "))
D = Dias * 60
Kmr = Km * 0.15
Dk = D+Kmr
print(f" O total a pagar é : {Dk:.2f}R$")
"""
# __________________________________________________________________________________________________________________
"""
# Quebrando um número
N = float(input("Digite um valor: "))
I = int(N)
print(f"O número digitado foi {N} e sua porção inteira é: {I}")
# Também podendo usar a biblioteca math e função trunc
# import math ---> e coloca depois math.trunc(N)
# from math import trunc ----> trunc(N) // Assim importando apenas a função que eu queira
"""
# __________________________________________________________________________________________________________________
"""
# Para iniciar uma lista e inserir valores dentro desta
# Para unir duas listas
list1 = []
seclist = []
result = []
for n in range(0, 5):
    lis = input("Digite letras: ")
    list1.append(lis)
# list2 = num.split(",")
print(list1)

# list3 = "->".join(list1)
# print(list3)

for n in range(0, 5):
    lis2 = input("Digite valores numéricos: ")
    seclist.append(lis2)
print(seclist)

for n in range(5):
    tupla = (list1[n], seclist[n])
    result.append(tupla)
print(result)
"""
# __________________________________________________________________________________________________________________
"""
list1 = []
seclist = []
soma = 0
for n in range(0, 5):
    lisv= int(input("Digite números: "))
    list1.append(lisv)
    soma = soma + lisv
# Para dizer o tipo da lista
print(type(lisv))
# Para mostrar a lista
print(list1)
# Para mostrar a soma dos números da lista
print(soma)
# Para inverter
print(list1[::-1])
"""
# __________________________________________________________________________________________________________________
"""
for n in range(3):
    idade = int(input("Digite um número: "))
    MaiorIdade = "Maior de idade" if idade >= 18 else "Menor de idade"
    # var = "Condição verdadeira
    print(MaiorIdade)
    print()
"""
# __________________________________________________________________________________________________________________
"""
i = 0
j = 10
while (i<9) and (j>1):
    print(i,j)
    i+=1
    j-=1
"""
# __________________________________________________________________________________________________________________
"""
CPF = 168.995.350-09
_____________________________
1 * 10 = 10
6 * 9 = 54
8 * 8 = 64
9 * 7 = 63
9 * 6 = 54
5 * 5= 25
3 * 4= 12
5 * 3= 15
0 * 2= 0

# PARA OBTER O 1 DÍGITO
     SOMA = 297
11 - (SOMA % 11) = 11
11 > 9 = 0 # Se o resultado for maior do que 9, então o dígito é zero
# Se o resultado for menor ou igual a 9, o dígito será o valor obtido
Dígito 1 = 0

_____________________________

# PARA OBTER O 2 DÍGITO

1 * 11 = 11
6 * 10 = 60
8 * 9 = 72
9 * 8 = 72
9 * 7 = 63
5 * 6 = 30
3 * 5 = 15
5 * 4 = 20
0 * 3 = 0
0 * 2 = 0

    SOMA = 343
11 - (SOMA % 11) = 9
Dígito 2 = 9
"""
"""
# Validador de cpf
cpf = [0, 3, 9, 2, 4, 8, 2, 0, 3]
soma = 0
nums = []
j = 0
for y in range(10, 1, -1):
    cpf = int(input("Digite cada número do cpf: "))
    nums.append(cpf)
    soma += y*nums[j]
    j+=1
print(nums)
print(soma)
"""
# __________________________________________________________________________________________________________________

# Validador de cpf
cpf = [0, 3, 9, 2, 4, 8, 2, 0, 3, 7, 6]
soma = 0
nums = cpf
nums.pop()
nums.pop()
j = 0

# Parte do primeiro número
print(nums)
for y in range(10, 1, -1):
    soma += y * nums[j]
    j += 1
print("Soma 1 é: ", soma)

result = (11 - (soma % 11))

if result > 9:
    nums.append(0)
else:
    nums.append(result)
print("Resultado do 1 dígito é: ", result)

# Parte do segundo número

soma = 0
i = 0
for z in range(11, 1, -1):
    soma += z * nums[i]
    i += 1
print("Soma 2 é: ", soma)
result2 = (11 - (soma % 11))
print("Resultado do 2 dígito é: ", result2)

if result2 >= 9:
    nums.append(0)
else:
    nums.append(result2)
print(nums)

if cpf == nums:
    print(f"Seu cpf {cpf} é valido;")
else:
    print("Quebrou meu código")

