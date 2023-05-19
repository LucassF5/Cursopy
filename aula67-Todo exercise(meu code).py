# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> add_wordr fazer café
# todo = ['fazer café', 'caminhar'] -> add_wordr caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import os


def limpa_tela():
    os.system("cls")


todo = []
desfazer = []


def mostra_itens(lista):
    for itens in lista:
        print(itens)
    print()


def add_word(nome, lista=None):
    if lista is None:
        lista = []
    elif nome == 'listar':
        mostra_itens(lista)
    lista.append(nome)
    print()
    return lista


def undo(lista):
    desfazer.append(todo[-1])
    lista.pop()
    print()
    return lista, desfazer


def refazer(lista):
    lista.append(desfazer[-1])
    desfazer.pop()
    print()
    return lista, desfazer


def roda_programa():
    while True:
        print('Comandos: listar, desfazer, refazer e clear')
        nome = input('Digite uma tarefa ou comando:\n>>> ')
        if nome == 'listar':
            print()
            mostra_itens(todo)

        elif nome == 'clear':
            limpa_tela()

        elif nome == 'desfazer':
            undo(todo)

        elif nome == 'refazer':
            refazer(todo)

        else:
            add_word(nome, todo)


roda_programa()
