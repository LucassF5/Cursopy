def repr_ligacao(cls):
    cls.__repr__ = tururu
    # O repr da classe vai ser a função meu_repr
    # Chamando a função tururu
    return cls

def tururu(self):
    self_class = self.__class__.__name__
    # guardando o nome da classe
    msg = f'Tururu {self_class}'
    return msg

@repr_ligacao
#Utilizando sintax sugar e decoradores
class CallPhone:
    def __init__(self, phone):
        self.phone = phone


call = CallPhone(123456789)
print(call)