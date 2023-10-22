# Abstração
# Herança - é um
# Polimorfismo - muitas formas
# Encapsulamento - esconder detalhes de implementação
# Mixin - é uma classe que não tem dependência de outras classes, mas que outras classes podem herdar dela
# Mixin não é uma classe que você instancia, é uma classe que você herda
# Mixin não deve ter dependência de outras classes
# Mixin não deve ser extendida
# Mixin não deve ter o método __init__

from pathlib import Path

# Forma com que o Django faz para pegar o caminho do arquivo
LOG_FILE = Path(__file__).parent / "log.txt"
# __file__ é o arquivo que está sendo executado


class Log:
    # def log(self, msg):
    def _log(self, msg):  # Deixando como protected
        raise NotImplementedError('Implemente o método log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
        # Vai exibir um erro e dizer em qual instância isso de originou
        # Self permite que a mensagem seja exibida na classe que usou o método

    def log_success(self, msg):
        return self._log(f'Success: {msg}')
        # Vai exibir uma mensagem de sucesso e dizer em qual instância isso de originou


class LogFileMixin(Log):
    # def log(self, msg):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print("\nSalvando no log:", msg_formatada)
        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')
        print("A mensagem foi salva")
        # print(msg)


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')
    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')
    # print(LOG_FILE) #Para ver o caminho do arquivo
