"""
Formatando valores com modificadores
:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f -   Quantidade de casas decimais
:(CARACTERE) (> ou < ou ^) (QUANTIDADE) (Tpo - s, d ou f)

> - ESQUERDA
< - DIREITA
^ - CENTRO
"""

num1 = 2035
print(f"{num1:0>10}")
# A quantidade de caracteres de num 1 já está incluso no 10

num2 = 135
print(f"{num2:5^10}")
print(f"{num2:0>7.3f}")

nome = 'Lucas'
sobrenome = "Franco"
sobrenome2 = "Rocha"
nome_format = "{2:*^15}   " "   {1:#^15} {0:^15}".format(nome, sobrenome, sobrenome2)
print(nome_format)
print(nome.ljust(30, '@')) # .ljust justifica à esquerda
print(sobrenome.rjust(30, '!')) # .rjust justifica à direita
print(sobrenome2.center(30, " ")) # .center centraliza
"""
Quando usar .rjust/ .ljust/ .center, lembrar de colocar no parêntesis o número correspondente à quantidade de
caracteres, seguido de vírgula, e o que deseja adicionar dentro de aspas
"""
nome3 = 'Lucas Franco RoCHa'
print(nome3.title()) # .tittle deixa as iniciais maiúsculas
print(nome3.upper()) # .upper deixa tudo maiúsculo
print(nome3.lower()) # .lower deixa tudo minúsculo


"""
Manipulando strings
* Strings indices
* Fatiamento de strings
* Funções built-in len, abs, type, print, etc ...
Essas funções podem ser usadas diretamente em cada tipo
"""
# Positivos [0,1,2,3,4,5...]
text = "Python"
# Negativos -[...5,4,3,2,1]
# Cada número corresponde à posição do caractere da str
# Igualmente nos negativos, porém no sentindo inverso (do final para o começo)
new_text = text[0:2]
# Quando quero delimitar um certo espaço de amostra de caracteres, uso o inicial, dois pontos(:) e 1 dígito a mais,
# subsequente do caracter final de sua escolha
print(f"Estou codando em {new_text}")
text2 = "LlUuCcAaSs"
new_new_text = text2[::2]
print(new_new_text)
# Para pular algum caractere da frase basta colocar o intervalo [x:y:z]
# Em que x é o inicial; y o final; e z o intervalo de cada "pulo"
"""
Obs: Caso deixe o espaço em branco:   
Em x: irá começar do caractere inicial
Em y: irá terminar no último caractere
Em z: o intervalo de "pulo" será de 1 em 1
"""
