"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca
        Contas têm agência, número da conta e saldo
        Conta (super classe) deve ter o método sacar abstrato (Abstração e
        polimorfismo - as subclasses que implementam o método sacar)
            Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
            ContaCorrente deve ter um limite extra
            Contas devem ter método para depósito

Pessoa (ABC)
    Cliente
        Clente -> Conta
            Criar classe Cliente que herda da classe Pessoa (Herança)
            Pessoa tem nome e idade (com getters)
            Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:


Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from abc import ABC, abstractmethod


class Conta(ABC):
    """
Conta (ABC)
    ContaCorrente
    ContaPoupanca
        Contas têm agência, número da conta e saldo
        Conta (super classe) deve ter o método sacar abstrato (Abstração e
        polimorfismo - as subclasses que implementam o método sacar)
            Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
            ContaCorrente deve ter um limite extra
            Contas devem ter método para depósito
    """

    def __init__(self, agencia, num_conta, saldo):
        self.agencia = agencia
        self.num_conta = num_conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: int | float):
        if valor > self.saldo or valor < 0:
            print(f"Não pode sacar um valor maior")
            return self.saldo

        print(f"Você sacou {valor} contos")
        self.saldo -= valor
        return self.saldo

    def depositar(self, valor: int | float) -> float:
        if valor < 0:
            return self.saldo

        self.saldo += valor
        print(f"{valor} contos depositados")
        return self.saldo


class ContaPoupanca(Conta):
    def __init__(self, agencia, num_conta, saldo):
        super().__init__(agencia, num_conta, saldo)

    def sacar(self, valor):
        if valor < 0:
            print("Poibido sacar valor menor que 0")
            return self.saldo

        elif valor > self.saldo * 1.5:
            print("Valor maior que o limite")
            return self.saldo

        print(f"Você tem um limite restante de {
              self.saldo*1.5 - self.saldo} e sacou {valor}")
        self.saldo -= valor
        return self.saldo


c = ContaPoupanca(1, 2, 3)
c.depositar(20)
print(c.saldo)
c.sacar(28)
print(c.saldo)
