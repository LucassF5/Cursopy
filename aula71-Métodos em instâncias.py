# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código

# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome_carro="Nome do carro"):
        # self.nome = 'Fusca' # Isso seria hard coded
        self.nome = nome_carro

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro(nome_carro='Celta')
print(celta.nome)
celta.acelerar()
Carro.acelerar(celta)
