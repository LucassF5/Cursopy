'''
nome = "Lucas"
idade = 21
altura = 1.72
peso = 62
ano_atual = 2022
imc = peso/(altura**2)
ano_nasc = ano_atual - idade

# obter o ano de nascimento
# obter o imc com duas casas decimais
# exibir um texto com todas as variáveis na tela usando f-strings

print("{0}, {1}, {2}, {3}, {4}, {5}, {6}".format(nome, idade, peso, altura, ano_atual, imc, ano_nasc))
print(f"{nome} tem {idade} anos, tem {altura} de altura e pesa {peso}kgs.")
print("O IMC de {} é {:.2f}".format(nome, imc))
print("{n} nasceu em {a}".format(n=nome, a=ano_nasc))
'''
"""
nome = 'Lucas'
sobrenome = "Franco"
sobrenome2 = "Rocha"
print(f"{nome}\n"+f"{sobrenome}\n"+f"{sobrenome2}\n")


nome3 = 'Lucas Franco RoCHa'
print(nome3.title())
"""
"""
x = int(input("A"))
while 10 < x <50:
    if x == 25:
        x = int(input("B"))
    print(x)
    x = x + 1
"""
'''
senha = input("Digite uma senha de 6 - 10 caracteres: ")
tam_senha = len(senha)
if tam_senha < 6 or tam_senha > 10:
    print("Repetir senha")
    nova_senha = input("")
else:
    ...
'''
"""
secreto = "Cachinhos"
secreto2 = "Princesinha"
secreto3 = "Farofinha"
secreto4 = "Amorzinho"
digitadas = []
chances = 5
print("Feliz dia dos namorados, pra começar esse dia bem nada melhor do que um teste não é? E que comecem os jogos")
print("   ")
print("Dica: Uma forma carinhosa que te chamo")
print("Dica2: Tem 9 letras")
print("Dica3: Eu adoro ficar pegando")
print("*Obs: começa com letra maiúscula")
print("   ")
while True:
    if chances <= 0:
        print("Você perdeu")
        break
    letra = input("Digite uma letra: ")
    if len(letra) > 1:
        print("Apenas uma letra")
        continue

    digitadas.append(letra)
    if letra in secreto:
        print(f"A letra {letra} existe na palavra")
    else:
        print(f"A letra {letra} não existe na palavra")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"

    if secreto_temporario == secreto:
        print("Você acertou")
        break
    else:
        print(f"A palavra secreta está assim: {secreto_temporario}")

    if letra not in secreto:
        chances -= 1
    print("Por favor, tente novamente")
    print()
    continue

digit = input("Agora escreva a palavra completa: ")
if digit == secreto:
    print(f"Parabéns meu amor, hoje é o nosso dia, sou muito feliz por te ter")
    print(f"{secreto}, casa gomigo pra sempre? <3 Te amo infinito")
"""
"""
import os
import time

def amo():
    for num in range(10):
        print("INGRID TE AMO SZ")
        time.sleep(0.5)

print("SISTEMA DA INGRID BONITINHA")
love = input("A Ingrid é muito linda? \n")
if love == "SIM":
    os.system("cls")
    amo()
"""
"""
import time
from turtle import *
color("red")
begin_fill()
pensize(3)
left(50)
forward(133)
circle(50,200)
right(140)
circle(50,200)
forward(133)
end_fill()
time.sleep(3)
"""
pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Franco',
    'idade': 21,
    'altura': 1.3,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ],
    'curso': "Eng. Elétrica"
}


"""
chave = 'Cor do tema'
pessoa[chave] = 'Azul'
"""
# Isso vai ser adicionado ao dicionário
'''
for chave in pessoa:
    print(chave)
print()

if pessoa.get("chave") is None:
    chave = 'Cor do tema'
    pessoa[chave] = 'Azul'
    print(pessoa[chave])
else:
    print("Já possui a chave")
'''
'''

a = [8,14,2,33,5,6,0,1,6,00,14]

sem_duplicatas = set()
ordenada = []
duplis = set()
duplis2 = []
first = []

def repetidos(list):
        for item in list:
            if item not in sem_duplicatas:
                ordenada.append(item)
                sem_duplicatas.add(item)

            else:
                duplis.add(item)
                duplis2.append(item)
        
        if duplis is None:
            print(-1)

        else:
            for num in list:
                if num in duplis2:
                    first.append(num)
        print(first[0])


repetidos(a)

# TENTATIVA ATIVIDADE SETS
# RESOLVER DEPOIS
'''
'''

def cria_matriz(num_linhas, num_colunas):
    matriz=[]
    for i in range(num_linhas):
        linha=[]
        for j in range(num_colunas):
            valor_colunas = int(input("NOtas: elemento [" + str(i) + "][" + str(j) + "] >>>"))
            linha.append(valor_colunas)
        matriz.append(linha)
    return matriz

cria = cria_matriz(1,3)
print(cria)
'''