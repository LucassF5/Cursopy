"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = "Python"
# Contador se faz com a função enumerate
for letra in texto:
    print(letra)
"""
for n, letra in enumerate(texto):
    print(n, texto)
"""
print("############")
for n in range(0, 100, 2):
    # 0 representa o start, que por convenção se deixar vazio representa início
    # 100 representa o espaço amostral
    # 2 é o step, se deixar vazio ele vai pular de 1 em 1, "pulo" de elementos
    if n % 8 == 0:
        print(n, "É múltiplo de 8")
print("##############")
texto = 'Python'
n_str = " "

for letra in texto:
    if letra == "t":
        # "continue", se usar isso vai pular esse laço e passar ao próximo
        # No caso se encontrar a letra t vai deixar sem e pular para o elif
        '''continue'''
        n_str = n_str+letra
    elif letra == "o":
        '''break'''
        # Usando o "break" irá encerrar o laço e quebrar a string somente até o ponto em que foi executada
        n_str += letra.upper()
    else:
        n_str += letra
        # Se nenhuma das condições anteriores for satisfeita o laço irá pular para a próxima letra
print(n_str)
print("##############")



