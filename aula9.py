"""
Listas em Python
Fatiamento
Append, insert, pop, del, clear, extend, min, max
range
"""
l1 = [0, 2, 4, 6]
l2 = [8, 10, 12, 14]
l3 = l1 + l2

l1.extend(l2)
# A função extend serviu para somar a lista l1 com os elementos da lista a2

l2.append(16)
# A função append insere um novo elemento à lista

l1.insert(8, "inserindo novo elemento")
# Insert acrescenta um novo elemento à lista, porém, podendo ser escolhida sua posição

l2.pop()
# Pop apaga o último elemento da lista ou algum que seja determinado

print(l1)
print(l2)
print(l3)
print(max(l3))
print(min(l3))
# Max e Min retornam os valores máximo e mínimos da função, ou seja, o último e o primeiro

del (l2[1:3])
# Del apaga elementos em um determinado espaço
print(l2)

l4 = range(0, 11, 2)
print(l4)
l4 = list(range(0, 11, 2))
print(l4)
# Range dá um alcance para determinada coisa, porém, somente se iterarmos e colocar "list" poderemos transformar
# em uma lista

soma = 0
for valor in l4:
    soma = valor + soma
    print(f'{soma} + {valor} = {soma}') # TEM ERRO
print(soma)

secreto = "lucas"
digitadas = []
chances = 5
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
    print(f"Você ainda tem {chances} chances")
    print()
