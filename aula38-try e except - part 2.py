# (Parte2) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError):
    print('TypeError + IndexError')
except Exception:  # Exception é a maior classe de erro, trata qualquer tipo de erro que não esteja sendo tratado
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
