from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo, nome):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.nome = nome

    def depositar(self, valor):
        self.saldo += valor
        print('\033[0;32mDepósito\033[m')
        self.detalhes()

    def detalhes(self):
        print(f'Seja bem vindo {self.nome} ao banco Python\n'
              f'Cliente: {self.nome}\n'
              f'Agência: {self.agencia}\n'
              f'Conta: {self.conta}\n'
              f'Saldo atual: {self.saldo}')

    @abstractmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insulficiente')
            print(f"{'-=' * 25}")
            return
        print(f"{'-=' * 25}")
        print('\033[0;34mSaque em conta Poupança\033[m')
        self.saldo -= valor
        self.detalhes()
        print(f"{'-=' * 25}")


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, nome, limite=100):
        super().__init__(agencia, conta, saldo, nome)
        self.limite = limite

    def sacar(self, valor):
        print(f"{'-=' * 25}")
        if self.saldo + self.limite < valor:
            print('Saldo insulficiente')
            return
        print('\033[0;33mSaque em Conta Corrente\033[m')
        self.saldo -= valor
        self.detalhes()
        print(f"{'-=' * 25}")
