import os


def limpa_tela():
    os.system("cls")


def mostra_enumerado(lista1):
    for valor, palavra in enumerate(lista1):
        print(valor, palavra)


def mostra_itens(lista1):
    for palavra in lista1:
        print(palavra)


def adiciona_tarefa(lista1, lista2, lista3):
    limpa_tela()

    palavra = input("\nO que deseja adicionar: ")
    lista1.append(palavra)

    if id(palavra) in lista2:
        print("Essa tarefa já está na lista")
        print("Retirando cópia")
        lista1.pop()
    else:
        ...
    lista2.append(id(palavra))


def apaga_tarefa(lista1, lista2, lista3):
    limpa_tela()

    print("\nQue item deseja retirar? (pelo número correspondente):\n ")
    mostra_enumerado(lista1)
    try:

        item = int(input("-> "))
        lista1.pop(item)
    except IndexError:
        print("Escolha um número válido")

    except ValueError:
        print("O programa só aceita números")


def edita_tarefa(lista1, lista2, lista3):
    limpa_tela()

    print("Qual deseja editar?")
    mostra_enumerado(lista1)
    try:

        index_lista = int(input("\nÍndice na lista:\n>>> "))
        nome_na_lista = input("\nNome na lista:\n>>> ")

        if nome_na_lista in lista1[index_lista]:

            if nome_na_lista in lista3:
                print()
            else:

                lista1[index_lista] = input("\nNovo nome:\n>>> ")
                palavra = lista1[index_lista]

                if id(palavra) in lista2:
                    print("Essa tarefa já está na lista")
                    print("Retirando cópia")
                    lista1.pop()

                else:
                    ...
                lista2.append(id(palavra))

        else:
            print("Escolha um número válido")

    except (ValueError, IndexError):
        print("Escolha uma opção válida")


def marca_concluido(lista1, lista2, lista3):
    limpa_tela()

    print("Qual deseja marcar como tarefa concluída?")
    mostra_enumerado(lista1)

    index_lista = int(input("\nÍndice na lista:\n>>> "))
    nome_na_lista = input("\nNome na lista:\n>>> ")
    try:
        if nome_na_lista in lista1[index_lista]:
            nome_inicial = lista1[index_lista]

            if "[X] " in lista3:
                lista1[index_lista] = nome_inicial
                print(nome_inicial)
                print("Essa tarefa já está marcada como concluída")
                print("Não pode ser marcada mais de uma vez")
                lista3.pop()

            else:
                lista1[index_lista] = '[X] ' + lista1[index_lista]
                ...

        else:
            print("Escolha um número válido")

    except IndexError:
        print("Escolha uma opção válida")

    except ValueError:
        print("O programa só aceita números")
        # AINDA REPETE SE ESTIVER MARCADA, RETIRA APÓS SEGUNDA VEZ


def roda_programa(lista1, lista2, lista3):
    while True:
        print()
        print("Escolha uma opção ")
        tarefaUser = input(
            "\n[i] inserir \n[a] apagar \n[l] listar  \n[e] editar \n[c] marcar como concluída  \n[s] para sair\n>>> ")

        if tarefaUser == 'i':
            adiciona_tarefa(lista1, lista2, lista3)

        elif tarefaUser == 'a':
            apaga_tarefa(lista1, lista2, lista3)

        elif tarefaUser == 'l':
            limpa_tela()
            mostra_itens(lista1)  # lista1

        elif tarefaUser == 'e':
            edita_tarefa(lista1, lista2, lista3)

        elif tarefaUser == 'c':
            marca_concluido(lista1, lista2, lista3)

        elif tarefaUser == 's':
            break

        else:
            print("Escolha [i], [a], [l], [e] ou [s]")


tarefa_casa = []
tarefas_trabalho = []
tarefas_escola = []

lista_tarefas = [tarefa_casa, tarefas_escola, tarefas_trabalho]

lista_todo_casa = []
id_lista_casa = []
tarefas_concluidas_casa = []

lista_todo_escola = []
id_lista_escola = []
tarefas_concluidas_escola = []

lista_todo_trabalho = []
id_lista_trabalho = []
tarefas_concluidas_trabalho = []

while True:
    print()
    # mostra(list)
    print("Qual tipo de lista deseja criar?")
    tarefaUser = input(
        "\n[c] casa \n[e] escola \n[t] trabalho \n[s] para sair\n>>> ")

    if tarefaUser == 'c':
        limpa_tela()
        roda_programa(lista_todo_casa, id_lista_casa, tarefas_concluidas_casa)

    elif tarefaUser == 'e':
        limpa_tela()
        roda_programa(lista_todo_escola, id_lista_escola,
                      tarefas_concluidas_escola)

    elif tarefaUser == 't':
        limpa_tela()
        roda_programa(lista_todo_trabalho, id_lista_trabalho,
                      tarefas_concluidas_trabalho)

    elif tarefaUser == 's':
        limpa_tela()
        print("Até logo")
        break

    else:
        print("Escolha [c], [e], [t] ou [s]")
