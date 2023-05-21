"""
Fazer um programa que peça o nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é muito curto";
se tiver 5 e 6 letras escreve "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande";
"""
nome = input("Escreva seu primeiro nome: ")
qtd_nome = len(nome)

if qtd_nome <= 4:
    print("Seu nome é muito curto")
elif (qtd_nome < 4) or (qtd_nome <= 6):
    print('Seu nome é normal')
else:
    print("Seu nome é muito grande")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex: Bom dia- 0 - 11; Boa tarde- 12 - 17; Boa noite- 18 - 23
"""
hora = int(input("Diga que horas são: "))

if 0 < hora < 12:
    print("Bom dia")
elif 12 < hora < 18:
    print("Boa tarde")
elif hora >= 24:
    print("Indique um horário válido") 
else:
    print("Boa noite")
"""
Faça um programa que peça ao usuário que digite um número inteiro, informe se este é par ou ímpar. Caso o usuário não 
digite um número inteiro, informe que não é um número inteiro.
"""
num = input("Digite um número inteiro: ")
if num.isdigit():
    num = int(num)

    if num % 2 == 0:
        print("Número par")
    else:
        print("Número ímpar")
else:
    print("Não é um número inteiro")
"""
Desafio de contadores
"""
i = 0
j = 10
while (i<9) and (j>1):
    print(i,j)
    i+=1
    j-=1




