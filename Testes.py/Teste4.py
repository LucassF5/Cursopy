import os

lista = []
while True:
    print()
    print("Escolha uma opção ")
    escolha=input("[i] inserir [a] apagar [l] listar ou [s] para sair:")
    if escolha == 'i':
        palavra = input("O que deseja adicionar: ")
        lista.append(palavra)
    
    elif escolha == 'a':
        print("Que item deseja retirar? (pelo número correspondente): ")
        for i, palavra in enumerate(lista):
            print(i, palavra)
        item = int(input("-> "))
        lista.pop(item)
    
    elif escolha == 'l':
        os.system("cls")
        for i, palavra in enumerate(lista):
            print(i, palavra)
    
    elif escolha == 's':
        break

    else:
        print("Escolha [i], [a] ou [l] ou [s]")
        