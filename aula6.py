"""
While / Else
Contadores
Acumuladores
"""
"""
contador = 1
acumulador = 1

while contador <= 15:
    print(contador, acumulador)

#    if contador > 5:
#       break

    acumulador = acumulador + contador
    contador += 1

else:
    print("Cheguei no else")
# Quando o contador chegar no último número irá sair do if e entrar no else
print("Terminou")
"""
"""
    if contador > 5:
       break
Se esse comando for ativado e parar o laço, o break não será executado por não ter atingido a condição
e tornado a expressão falsa
Em outras palavras, se quebrar o laço no meio do caminho não executa o else
"""
# Independente do break ou não, essa mensagem será executada por não fazer parte do comando if

# Iteração - se os elementos possuírem índices
# Índices = 0123456789........N (Tendo começo e/ou fim) É possível colocar em um loop
frase = "o rato roeu a roupa do rei de roma"
tam_frase = len(frase)
contador = 0
nova_string = " "
'''
while contador < tam_frase:
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
'''

input_do_user = input("Qual letra deseja colocar?: ")

while contador < tam_frase:
    letra = frase[contador]
    if letra == input_do_user:
        nova_string += input_do_user.upper()
    else:
        nova_string += letra
    contador += 1
print(nova_string)
"""
frase = "Contar elementos da string"
tam_frase = len(frase)
contador = 0

while contador < tam_frase:
    print(frase[contador], contador)
    contador += 1
"""

