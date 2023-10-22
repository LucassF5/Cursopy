from log import LogFileMixin, LogPrintMixin


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
        # if self._ligado == False:
        #     self._ligado = True
        #     print(f"Ligando {self._nome}")

        # else:
        #     print("O aparelho já está ligado")

    def desligar(self):
        if self._ligado:
            self._ligado = False
        # if self._ligado == True:
        #     self._ligado = False
        #     print(f"Desligando {self._nome}")

        # else:
        #     print("O aparelho já está desligado")


class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f"{self._nome} está ligado"
            self.log_success(msg)

    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f"{self._nome} está desligado"
            self.log_error(msg)


# geladeira = Eletronico("geladeira")
# geladeira.ligar()
# geladeira.ligar()
