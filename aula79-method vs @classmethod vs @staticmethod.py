# method vs @classmethod vs @staticmethod

# method - self, método de instância
# Método que recebe self no primeiro parâmetro e tem acesso a tudo da instância(atributos e métodos)

# @classmethod - cls, método de classe
# Recebe cls no primeiro parâmetro, a própria classe

# @staticmethod - método estático (❌self, ❌cls)
# Não tem acesso ao self e  nem a cls

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    # setter
    # Configura o valor de um atributo qualquer
    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('LOG:', msg)


def connection_log(msg):
    print('LOG:', msg)


# c1 = Connection()
c1 = Connection.create_with_auth('luiz', '1234')
# c1.set_user('luiz')
# c1.set_password('123')
print(Connection.log('Essa é a mensagem de log'))
print(c1.user)
print(c1.password)
