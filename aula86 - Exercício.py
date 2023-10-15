class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._fabricante = None
        self._motor = None

    @property  # Getter
    def motor(self):
        return self._motor

    @motor.setter  # Setter
    def motor(self, valor):
        self._motor = valor

    @property  # Getter
    def fabricante(self):
        return self._fabricante

    @fabricante.setter  # Setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


Onix = Carro("Ônix")
GM = Fabricante("Chevrolet")
Onix.fabricante = GM
motor_1_0 = Motor("1.0")
Onix.motor = motor_1_0
print(Onix.nome, Onix.motor.nome, Onix.fabricante.nome)

Argo = Carro("Argo")
Fiat = Fabricante("FIAT")
Argo.fabricante = Fiat
motor_1_0 = Motor("1.0")
Argo.motor = motor_1_0
print(Argo.nome, Argo.motor.nome, Argo.fabricante.nome)

Hillux = Carro("Hillux")
Toyota = Fabricante("Toyota")
Hillux.fabricante = Toyota
motor_3_8 = Motor("3.8")
Hillux.motor = motor_3_8
print(Hillux.nome, Hillux.motor.nome, Hillux.fabricante.nome)
