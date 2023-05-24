import json

from aula76_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    # Expandindo dicionário para poder selecionar e fazer o carregamento de arquivos
    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
