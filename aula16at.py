"""
Criar funções que duplicam, triplicam e quadriplicam o número recebido como parâmetro
"""
def equacao(multiplicador):
    def mult(num):
        return multiplicador*num
    return mult

mult_por_2 = equacao(2)
mult_por_3 = equacao(3)
mult_por_4 = equacao(4)
print(mult_por_2(10))
print(mult_por_3(20))
print(mult_por_4(50))

for n in [3,5,15,20]:
    print(mult_por_2(n))
