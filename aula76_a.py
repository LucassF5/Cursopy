# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

CAMINHO_ARQUIVO = 'aula76.json'


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


p1 = Pessoa("Lucas", 21)
p2 = Pessoa("Maria", 54)
p3 = Pessoa("LuF", 19)
bd = [vars(p1), p2.__dict__, p3.__dict__]


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        json.dump(bd,
                  arquivo,
                  ensure_ascii=True,
                  indent=2)


# Caso este arquivo seja o primeiro a ser executado, __main__, então há o dump do arquivo
if __name__ == "__main__":
    print('ELE É O __main__')
    fazer_dump()
