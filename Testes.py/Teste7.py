class Carro:
    def __init__(self, nome, ligado=False) -> None:
        self.nome = nome
        self.ligado = ligado

    @property
    def ligar_carro(self):
        if not self.ligado:
            self.ligado = True
            print(f'{self.nome} está LIGADO')
            return
        else:
            print("Carro já está ligado")

    @property
    def desligar_carro(self):
        if self.ligado:
            self.ligado = False
            print(f'{self.nome} está DESLIGADO')
            return
        else:
            print("Carro já está desligado")


c1 = Carro("Celta")
c1.ligar_carro
c1.ligar_carro
c1.desligar_carro
c1.desligar_carro
