# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos
# apenas implementando os dunder methods que o
# Python vai usar.
# Isso é chamado de Duck typing. Um conceito
# relacionado com tipagem dinâmica onde o Python não
# está interessado no tipo, mas se alguns métodos existem
# no seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o
# traceback. Se ele retornar True, exceção no with será
# suprimidas.
#
# Ex:
# with open('aula149.txt', 'w') as arquivo:
#     ...
class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
                     #Classe da exceção,  exceção
        print('FECHANDO ARQUIVO')
        if self._arquivo is not None:
            self._arquivo.close()


with MyOpen('aula96.txt', 'w') as arquivo:
    arquivo.write('Entrando no arquivo\n')
    arquivo.write('Dia 29/12/2023\n')
    arquivo.write('Fazendo testes\n')
    print('WITH', arquivo)


# class MyContextManager():

#     def __init__(self):
#         print("ENTRANDO NO INIT")

#     def __enter__(self):
#         print("ENTROU NO ENTER")
#         return "TESTE PARA SABER SE ENTROU"
    
#     def __exit__(self, class_exception, excetion_, traceback_):
#         print("SAINDO DO ARAQUIVO -> EXIT")
#         return "SAIU DO ARQUIVO"

# instancia = MyContextManager()
# with instancia as arquivo:
#     print("WITH", arquivo)