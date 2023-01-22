# Para fazer comentários são utilizados ###
"""
Aspas duplas ou simples em trios também podem ser usadas como comentários
Mas não são realmente comentários
"""

# Strings podem ser identificadas usando aspas duplas e ou simples
print("Exemplo 1")
print('Exemplo 2')
# Ou conjugadas, porém o compilador inicia a leitura e termina com o mesmo tipo que começou
print("Se começou com'aspas duplas' ele vai ler até a outra")
print('E "vice" versa')
"""
Porém, pra sair de uma situação com muitas aspas é utilizado \\  uma barra invertida, anulando o símbolo posterior \\
"""
print("Outro \' exemplo \' teste")
"""
Porém, a barra invertida é lida
Caso use (\') barra invertida e n (\n), vai acontecer uma quebra de linha
Se colocar um r antes da string (str) vai informar para não executar nenhuma ação mostrada, e sim tratar como exemplo
... e  ler a sentença completa como string
"""
print(r"Exemplo \'teste\' 2")
"""
Tipos de dados
str - string - textos "Exp1" 'Exp2'
int - inteiro (números inteiros) - 1 2 50 687
float - números reais/ ponto flutuante - 10.3 20.76 -325.4 0.0
bool - booleano/lógico - True/False 10 == 10
"""
# Type casting - conversão de tipos
print('Lucas', type('Lucas'))
# Type serve pra dizer o tipo de dado que está sendo apresentado
print('Lucas', type('Lucas'), bool('Lucas'))
# Colocando o tipo bool logo após está alterando o tipo de informação
print('2', type('2'), type(int('2')))
# Ou também é possível alterar no momento em que é perguntado o tipo

# Str: nome
print("Lucas", type("Lucas"))
# Int: idade
print(20, type(20))
# Float: altura
print(1.72, type(1.72))
# Bool: maior de idade - x>18
print(20>18, type(20>18))

"""
Operadores aritméticos
+ adição; - subtração; * multiplicação; / divisão; 
// divisão truncada/inteira; ** exponenciação; % resto; () alterar precedência
"""
print(2 * "Lucas") # O operador de multiplicação pode ser usado pra repetição em conjunto com strs
print("Lucas" + "!!!") # O operador de soma pode juntar duas sentenças = Concatenação

nome="Lucas"
idade=20
altura=1.72
peso=62
imc= peso/(altura**2)
print(nome, "tem", idade, "anos de idade e seu imc é", imc)
print(f"{nome} tem {idade} anos de idade e seu imc é {imc}")
print("{} tem {} anos de idade e seu imc é {:.2f}".format(nome, idade, imc))
"""
\'Usando o f antes da sentença e colocando tudo em aspas duplas é possível fazer uma formatação de strings
Sendo assim feita utilizando as chaves e inserindo assim variáveis dentro\'
\'Outra forma é utilizando o format
Vem logo no final da sentença, abre os parêntesis e coloca as variáveis na ordem para aparecer
Sendo definido pela ordem (o,1,2...) ou  também pode ser definido outras variáveis para simplificar e poder colocar 
na ordem desejada\'
"""

