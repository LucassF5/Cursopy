"""
While -
Utilizado para realizar ações enquanto uma condição for verdadeira
"""
'''
x = 0
while x < 20:
    if x ==10:
        x = x + 2
        continue
        # Ao usar continue a operação retorna ao laço, não passando por operações posteriores
    print(x)
    x += 1 # x = x + 1
    # Equivale a x = x + 1, pois indica que o valor x irá somar + 1 ao valor anterior
"""
Quando x se torna igual a 10 ele entra na condição IF e atribui um novo valor à variável
Assim, dando um novo valor a 10 e fazendo com que ele seja 'pulado', indo para 12 (10 + 2)
### Esse novo 'x = x + 2' só vai valer pra quando o valor de x atingir 10
"""
print("It's over!!!")
# O comando continue é usado para continuar o código quando este atinge uma determinada condição
# O comando break, assim como o continue, irá ser executado quando atingir uma condição, mas irá encerrar o laço
'''
'''
x = 0
while x < 5:
    y = 0
    while y < 4:
        z = 0
        while z < 3:
            print(f"({x},{y},{z})")
            z += 1

        y += 1
    x += 1
'''
'''
Seguindo a ordem de precedência, x só será executado após terminar a sequência de y, e o mesmo acontece com y e z
Antes de iniciar qualquer while é necessário definir a variável a ser utilizada
Caso a variável que vai entrar no segundo e/ou terceiro while fosse definida fora, assim como x, elas não zerariam e 
retornariam valores sempre que fosse adicionado +1 à sua antecessora
'''
while True:
    print()
    n1 = input('Digite um número: ')
    n2 = input("Digite outro número: ")
    ope = input("Digite um operador: ")

    if not n1.isnumeric() or not n2.isnumeric():
        print("Você precisa digitar um número")
        continue
    n1 = int(n1)
    n2 = int(n2)
    # + - / // * **
    if ope == "+":
        print(n1 + n2)
    elif ope == "-":
        print(n1 - n2)
    elif ope == "/":
        print(n1 / n2)
    elif ope == "*":
        print(n1 * n2)
    else:
        break

    sair = input("Deseja sair? [s] sim ou [n] não: ")
    if sair == "n":
        continue
    else:
        break
