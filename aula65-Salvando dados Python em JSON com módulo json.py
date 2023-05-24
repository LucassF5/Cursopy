# json.dump = Gera um arquivo json
# json.dumps = carrega um dump para uma str
# json.load

import json

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'Franco',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

# JSON carrega os caracteres como ASCII invés da codificação de caracteres padrão da sua máquina
with open('aula65.json', 'w', encoding='utf8') as arquivo:
    json.dump(
        pessoa,
        arquivo,
        ensure_ascii=False,  # Aqui é para desativar o carregamento em ascii e mandar normal
        indent=2,  # Indent deixa o arquivo formatado
    )

with open('aula65.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
