# Empacotamento e desempacotamento de dicionários

# pessoa = {
#     'nome' : 'Aline',
#     'sobrenome' : 'Souza'
# }

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)


pessoa = {
    'nome' : 'Aline',
    'sobrenome' : 'Souza'
}

dados_pessoa = {
    "idade" : 20,
    "altura" : 1.7
}

pessoa_completa = {**pessoa, **dados_pessoa ,"tamanho_pé": 38}
# Para adicionar dicts dentro de outros basta colocar ** e o nome do que quer inserir

print(pessoa_completa, "\n")
# ---------------------------------------------------
for chave in pessoa_completa:
    print(f'{chave}: {pessoa_completa[chave]}')
print()
# ---------------------------------------------------
for chave, valor in pessoa_completa.items():
    print(chave,":", valor)
# ---------------------------------------------------

# Acima duas formas de exibir dicts

print()

def mostra_argumentos_nomeados(*args, **kwargs):
    if args is not None:
        print("NÃO NOMEADOS: ", args)

    for chave, valor in kwargs.items():
        print(chave, valor)

# Ex1: 
mostra_argumentos_nomeados(1,2,4,3,nome = "Lucas", qualquer = 7654534)
# Os primeiros números não foram identificados e entraram como argumentos não nomeados
# Como foram nomeados e identificados eles entraram no for
print()
# Ex2: 
mostra_argumentos_nomeados(**pessoa_completa)

