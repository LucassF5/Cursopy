"""
For / ELse em Python
"""
var = ["Lucas", "Franco", "Rocha"]

for valor in var:
    if valor.startswith("L"):
        # (.startswith) É usado para verificar se há algo na lista começando com tal letra
        print(valor, "começa com 'L'")
    else:
        print(valor, "não começa com 'L'")
start_com_l = False
for valor in var:
    if valor.lower().startswith("j"):
        start_com_l = True
    # Colocando o .lower vai transformar todas as letras em minúsculas e assim checar todas as palavras
if start_com_l:
    print("Existe uma palavra começando com L")
else:
    print("Não existe uma palavra começando com L")

# Tirando a variável para começar com "L"
for valor in var:
    if valor.lower().startswith("l"):
        break
        #  Assim não apresentará nada quando uma palavra começar com a letra L
else:
    print("Não existe uma palavra começando com L")
