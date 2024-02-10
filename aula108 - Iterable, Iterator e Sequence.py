# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html
from collections.abc import Sequence

# Iterator precisa implementar __iter__

# Iterable precisa implementar __next__
# Só que o __next__ do Iterable é o __getitem__ do Iterator

# Sequence precisa implementar __len__ e __getitem__
# Só que o __getitem__ do Sequence é o __iter__ do Iterable


class MyList(Sequence):
    def __init__(self):
        self._data = {} # Utilizando um dicionário para armazenar os valores
        self._index = 0 # Utilizado para controlar a quantidade de valores
        self._next_index = 0 # Utilizado para controlar o __next__

    def append(self, *values): # Método para adicionar valores
        for value in values:
            self._data[self._index] = value
            self._index += 1

    def __len__(self) -> int: 
        # Método para retornar a quantidade de valores
        return self._index

    def __getitem__(self, index): 
        # Método para retornar um valor específico
        return self._data[index]

    def __setitem__(self, index, value):
        # Método para alterar um valor específico
        self._data[index] = value

    def __iter__(self):
        return self

    def __next__(self): 
        
        if self._next_index >= self._index:
            self._next_index = 0
            raise StopIteration

        value = self._data[self._next_index]
        self._next_index += 1
        return value


if __name__ == '__main__':
    lista = MyList()
    lista.append('Maria', 'Helena')
    lista[0] = 'João'
    lista.append('Luiz')
    # print(lista[0])
    # print(len(lista))
    for item in lista:
        print(item)
    print('---')
    for item in lista:
        print(item)
    print('---')