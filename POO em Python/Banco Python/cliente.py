class Pessoa:
    def __init__(self, nome, idade, numero, endereco, uf, cpf):
        self._nome = nome
        self._idade = idade
        self._numero = numero
        self._endereco = endereco
        self._uf = uf
        self._cpf = cpf

    def mostra_cadastro(self):
        print(f"{'-=' * 25}")
        print('\033[0;36mCliente cadastrado no banco Python\033[m')
        print(f'Nome: {self._nome} Idade: {self._idade}\n'
              f'Número: {self._numero}\n'
              f'Endereço: {self._endereco} UF: {self._uf} \n'
              f'CPF: {self._cpf}\n')

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade, numero, endereco, uf, cpf):
        super().__init__(nome, idade, numero, endereco, uf, cpf)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta
