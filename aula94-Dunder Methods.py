# Teoria: python Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str  # __repr__ é para desenvolvedores

class Ponto:
    def __init__(self, x, y, z="String"):
        self.x = x
        self.y = y
        self.z = z

    # __str__ chama a representaçãp de string do objeto
    def __str__(self):
        return f"(x={self.x}, y={self.y})"
    
    #Caso o __str__ não exista ele chama o __repr__ por fallback
    # __repr__ é para desenvolvedores
    def __repr__(self) -> str: #__repr__ significa reprentação
        # -> indica que o método retorna uma string
        # class_name = self.__class__.__name__ # Vai retornar o nome da classe
        class_name = type(self).__name__ # Também retorna o nome da classe
        return f"{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})"
        #Utilizando !r mostra para o outro desenvolvedor o "tipo"
    
    def __add__(self, other):
        novo_x = self.x + other.x
        novo_y = self.y + other.y
        return Ponto(novo_x, novo_y)

    def __gt__(self, other):
        resultado_self = self.x + self.y
        resultado_other = other.x + other.y
        return resultado_self > resultado_other

    
p1 = Ponto(1,2)
p2 = Ponto(3,4)
print(p1) #Retorna um str
print(repr(p2)) #Retorna um repr
#Para visualizar o repr basta usar sua funçã
print(f"{p1!s}") 
print(f"{p2!r}") 
#Utilizando !r para repr e !s para string pode ser visualizado

if __name__ == '__main__':
    p1 = Ponto(4, 2)  # 6
    p2 = Ponto(6, 4)  # 10
    p3 = p1 + p2
    print(p3)
    print('P1 é maior que p2', p1 > p2)
    print('P2 é maior que p1', p2 > p1)