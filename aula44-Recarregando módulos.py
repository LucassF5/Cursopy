import importlib  # biblioteca que permite mainupular importação de bibliotecas

# O Python ao importar uma biblioteca só carrega uma vez, sendo necessário recarregar para utilizar novamente

# import aula

# print(aula1.nome)

for i in range(10):
    # importlib.reload(aula1) ## Reload permite recarregar a biblioteca mais de uma vez
    print(i)

print('Fim')
