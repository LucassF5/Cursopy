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
    print(lista)


def add_word(nome, lista=None):
    if lista is None:
        lista = []
    elif nome == 'listar':
        mostra_itens(lista)
    lista.append(nome)
    return lista


def undo(lista):
    desfazer.append(todo[-1])
    lista.pop()
    return lista, desfazer


def refazer(lista):
    lista.append(todo[-1])
    desfazer.pop()
    return lista, desfazer


def roda_programa():
    while True:
        nome = input(">>> ")
        if nome == 'listar':
            mostra_itens(todo)
            print('\n\n')
            mostra_itens(desfazer)
        elif nome == 'limpar':
            limpa_tela()
        elif nome == 'desfazer':
            undo(todo)
        elif nome == 'refazer':
            refazer(todo)
        else:
            add_word(nome, todo)


roda_programa()
