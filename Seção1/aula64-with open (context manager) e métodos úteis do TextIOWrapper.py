#  Criando arquivos com Python + Context Manager with
# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')
#
# arquivo.close()

# with open(caminho_arquivo, 'w') as arquivo:
#     print('Olá mundo')
#     print('Arquivo vai ser fechado')

# Caso já tenha um arquivo e por acaso abra este arquivo com m novamente, todas as informações serão apagadas
# w apaga para ser reescrito tudo novamente
with open(caminho_arquivo, 'w+', encoding='utf8') as arquivo:  # w+ serve para escrita e leitura
    # Habilitando o encoding como 'utf8'/'utf-8' declaramos que vai poder mostrar acentos ou ç
    arquivo.write('Linha 1\n')  # Usando o nome do arquivo e write para escrever
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)  # Move o cursor de acordo com as coordenadas dadas
    # Readline é parecido com next, só lê uma linha por vez
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())
    # Usando end ou strip pode-se parar a quebra de linha que o readline dá

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():  # Usando readlines pode-se ler mais de uma linha por vez
        print(linha.strip())


print('#' * 10)  # Como está fora do with open então não vai entrar no arquivo

with open(caminho_arquivo, 'r') as arquivo:  # Abrindo arquivo no modo de leitura
    print(arquivo.read())  # Imprimindo no terminal o que é dito no arquivo

# os.remove(caminho_arquivo) # ou unlink
# Remove ou unlink apagam o arquivo

# os.rename(caminho_arquivo, 'aula116-2.txt')
# Rename renomeia o arquivo
