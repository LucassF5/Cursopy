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

import json
import os


def limpa_tela():
    os.system("cls")


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


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados


CAMINHO_ARQUIVO = 'aula67.json'
todo = ler([], CAMINHO_ARQUIVO)
desfazer = []


# def roda_programa():
while True:
    print('Comandos: listar, desfazer, refazer, clear e sair')
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

    elif nome == 'sair':
        break

    else:
        add_word(nome, todo)
    salvar(todo, CAMINHO_ARQUIVO)
