# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

# getter -> obter valor
# getter -> enviar valor

class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        # self._alguma coisa é um atributo protegido pela classe, ou seja, uso exclusivo dela
        self._cor_tampa = None
        # isso é uma convenção
        # Não utilize este atributo, protegido pela classe

    @property  # É um método, método não guarda/salva valor, apenas EXECUTA ações
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter  # decorator que define como setter
    def cor(self, valor):
        # Setter é um método que precisa de self e uma variável para receber um valor
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)
