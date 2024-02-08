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

    def __init__(self, agencia:int, num_conta:int, saldo:float=0):
        self._agencia = agencia
        self.num_conta = num_conta
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_valor):
        self.__saldo = novo_valor

    @property
    def agencia(self):
        return self._agencia
    
    @agencia.setter
    def agencia(self, num_agencia):
        self._agencia = num_agencia

    # @property
    # def num_conta(self):
    #     return self.num_conta

    @abstractmethod
    def sacar(self, valor):
        if valor > self.saldo or valor < 0:
            print(f"Não pode sacar um valor maior")
            print("MÉTODO PAI")
            return self.saldo

        print(f"Você sacou {valor} contos")
        print("MÉTODO PAI")
        self.__saldo -= valor
        return self.__saldo

    def depositar(self, valor) -> float:
        if valor < 0:
            return self.__saldo

        self.__saldo += valor
        # print(f"{valor} contos depositados")
        return self.__saldo



class ContaPoupanca(Conta):
    def __init__(self, agencia=123, num_conta=321, saldo=0) -> None:
        super().__init__(agencia, num_conta, saldo)


    def sacar(self, valor: float) -> float:
        if valor > 0:
            self.saldo -= valor
            # print("MÉTODO FILHO")
            print("Saque bem sucedido!")
            return self.saldo
        # print("MÉTODO FILHO")
        # print(f"Valor {valor} inválido ou sem limite")
        return self.saldo
    
    def __repr__(self) -> str:
        return f"ContaPoupanca(agencia={self.agencia}, num_conta={self.num_conta}, saldo={self.saldo})"


class ContaCorrente(Conta):
    def __init__(self, agencia=1010, num_conta=2020, saldo=0, limite:float=100) -> None:
        super().__init__(agencia, num_conta, saldo)
        self.limite = limite

    def sacar(self, novo_valor:  float) -> float:
        if  0 < novo_valor <= self.limite:
           self.saldo -= novo_valor
           print(f"{novo_valor} sacados, limite restante {self.limite - novo_valor}")
           return self.saldo
            
        print(f"Valor {novo_valor} inválido") 
        return self.saldo
     

    def __repr__(self) -> str:
        return f"ContaCorrente(agencia={self.agencia}, num_conta={self.num_conta}, saldo={self.saldo})"
    

class Pessoa():

    # Pessoa (ABC)
    #       Cliente
    #         Clente -> Conta
    #         Criar classe Cliente que herda da classe Pessoa (Herança)
    #         Pessoa tem nome e idade (com getters)
    #         Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade:int):
        self.idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, conta: Conta) -> None:
        super().__init__(nome, idade)
        self.conta = conta

    def __repr__(self) -> str:
        return f"Cliente(nome={self.nome}, idade={self.idade}, conta={self.conta})"
    
    # def sacar(self, valor):
    #     return self.conta.sacar(valor)

class Banco():

    """
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
    
    def __init__(self) -> None:
        pass


c = ContaCorrente()
c.depositar(100)
c.sacar(50)