"""
Funções = def em Python
"""
"""
def saudacao():
   print("Olá mundo")

saudacao()
# ---------------------------
"""
"""
def saudacao(msg):
    # msg recebe o valor da str contida no print
    print(msg)
saudacao("Hi")
# Obrigatório colocar a var msg dentro da função, ou uma mensagem para atribuir valor
# A str está sendo absorvida pela var msg
# ---------------------------
"""
"""
def saudacao(msg, nome):
    print(msg, nome)

saudacao("Olá","Lucas")
saudacao("Hello","World")
# ---------------------------
"""
"""
def saudacao(msg="Hi", nome="Lucas"):
    # Trocando uma letra por um valor de minha preferência
    nome = nome.replace("a", "4")
    msg = msg.replace("e", "3")
    # Definindo valores para a variável, caso o usuário não digite nada
    print(msg, nome)

saudacao()
saudacao(nome="Maria", msg="Aoba")
# Caso queira inverter a ordem pode-se simplesmente declarar o nome das variáveis na chamada da função(nomeando-as)
saudacao(msg="Aoba")
# Se quiser renomear apenas uma função, então declara-se essa, sem colocar valor para a outra
saudacao("Olá", "Lucas")
saudacao("Hello", "World")
# ---------------------------
"""
"""
def saudacao(msg="Hi", nome="Lucas"):
    nome = nome.replace("a", "4")
    msg = msg.replace("e", "3")
    return f"{msg} {nome}"

var = saudacao()
print(var)
# ---------------------------
"""
