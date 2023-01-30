# frases = {}
# frases.update({
#     "vida" : "mi bida",
#     "amor" : "mi amor"

# })
# qtd_vezes_update = int(input("Quantidade de chave-valor inserir: "))
# for num in range(qtd_vezes_update):
#     chave = input('Chave\t>>>')
#     frases[chave] = input("Valor\t>>> ")
#     print()

# # frases['sobrenome'] = 'Franco'

# for chave in frases:
#     print(chave,":", frases[chave])

# print("\tO")
# print("       /|\\")
# print("       / \\") # Pessoa pra jogo da forca


import os
import time


secreto = input("Digite a senha: ")
print("Memorizou?")
time.sleep(1)
print("Apagando")
print("...")
time.sleep(1)
os.system("cls")

digitadas = []
chances = 7

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
    print(f'Você tem {chances} chances' )

    if chances == 6:
        print()
        print("A partir da próxima você começa no jogo da forca")
        continue
    elif chances == 5:
        print("\tO")
    elif chances == 4:
        print("\tO")
        print("        |")
    elif chances == 3:
        print("\tO")
        print("       /|")
    elif chances == 2:
        print("\tO")
        print("       /|\\")
    elif chances == 1:
        print("\tO")
        print("       /|\\")
        print("       /")
    elif chances == 0:
        print("\t__")
        print("       | !")
        print("       | 0")
        print("       |/|\\")
        print("       |/ \\")
        print("E morreu!!!")
