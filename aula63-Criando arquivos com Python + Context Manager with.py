# Criando arquivos com Python + Context Manager with
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

# Se não colocar o caminho ele vai criar na mesma pasta do arquivo criador
file_path = 'C:\\Users\\franc\\OneDrive\\Documentos\\cursopy\\Seção1\\'
# USAR DUAS BARRAS INVERTIDAS PARA NÃO DAR ERRO DE CAMINHO NO WINDOWS
file_path += 'Abrindo arquivo'
# Obs: colocando o final do arquivo, como ".py ou .txt" cria um arquivo de modo escolhido

# file = open(file_path, 'w')  ## w do modo de escrita
# print("Abrindo arquivo com Python")
# file.close()  ## Nunca esquecer de fechar o arquivo

with open(file_path, 'w') as file:
    print("Abrindo arquivo")
# Com with não precisa se preocuopar em colocar .close()
