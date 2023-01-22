"""
Função len - utilizada para fazer leitura de dados
NÃO funciona com tipos numéricos
É contado todos os caracteres, incluindo espaços
Retorna um número inteiro informando a quantidade
"""
usuario = input('Digite o nome de usuário: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))
if qtd_caracteres < 6:
    print("Digite mais de 6 caracteres")
else:
    print("Você foi cadastrado")

usuario1 = input('Digite o nome do 1º usuário: ')
usuario2 = input('Digite o nome do 2º usuário: ')

print(f"A quantidade de caracteres digitados foi: {len(usuario1) + len(usuario2)}")
"""
isnumeric isdigit isdecimal
Funções que servem para auxiliar e evitar erros no programa
Servem para verificar se a STRING possui números e convertê-los em INTEIROS
Só valem para inteiros e positivos
"""
"""
Usando pass e ellipsis
Quando em um if, deixar para botar o print depois
"""
valor = True
if valor:
#Posso usar "pass" ou "..."(ellipsis)
    ...
else:
    print('Foi isso')
