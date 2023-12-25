# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID

#                                   Princípio da substituição de liskov
#                           Objetos de uma superclasse devem ser substituíveis
#                           por objetos de uma subclasse sem quebrar a aplicação.

# Sobrecarga de métodos (overload)  🐍 = ❌
#Python não suporta sobrecarga de métodos, pois a cada método criado, o anterior é sobrescrito.
# Sobreposição de métodos (override) 🐍 = ✅

from abc import ABC, abstractmethod


class Notificacao(ABC):
    #Classe abstrata
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    #Método abstrato
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    #Classe concreta - implementando o método abstrato e herdando da classe abstrata
    def enviar(self) -> bool:
        #-> bool é uma type hint/annotation
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    #Classe concreta - implementando o método abstrato e herdando da classe abstrata
    def enviar(self) -> bool:
        #-> bool é uma type hint/annotation
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)
