# Context Manager com função - Criando e Usando gerenciadores de contexto

from contextlib import contextmanager
#Diferente de usar classe aqui não continua caso ocorra uma exceção

@contextmanager
def my_open(caminho_arquivo, modo): #Utilizando o generator contextmanager
    try: #Abrindo
        print('ABRINDO ARQUIVO')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo #pausa a execução do código para executar o with
    # except Exception as e: #Sem tratar a exceção
    #     print('FECHANDO ARQUIVO')
    finally: #Fechando a exceção
        arquivo.close() #type:ignore   #sempre será executado

    

with my_open('aula97.txt', 'w') as arquivo:
    arquivo.write('Abrindo novo no arquivo\n')
    arquivo.write('Dia 03/01/2023\n')
    arquivo.write('Fazendo testes\n')
    print('WITH', arquivo)