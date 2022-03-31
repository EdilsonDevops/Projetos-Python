from banco import Banco
from cliente import Cliente, Pessoa
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

# Inserir o cliente
# Informe Nome, Idade, Número, Endereço, UF e CPF
cliente1 = Cliente('Edilson', 22, '(11) 99999-9999', 'Rua osvaldo cruz 13', 'SP', '255.555.255-12')
cliente2 = Cliente('Alfredo', 50, '(11) 98888-8888', 'Rua paulista 63', 'RJ', '275.575.277-11')
cliente3 = Cliente('Fabio', 22, '(11) 99999-9999', 'Rua flavio cordeiro 88', 'MG', '789.522.222-88')

# Mostra cadastro
Pessoa.mostra_cadastro(cliente1)
Pessoa.mostra_cadastro(cliente2)
Pessoa.mostra_cadastro(cliente3)
print(f"{'-=' * 25}")

# Inserir a conta
# Informe Agência, Conta, Saldo e Nome)
conta1 = ContaPoupanca(1111, 254136, 0, cliente1.nome)
conta2 = ContaCorrente(2222, 254137, 0, cliente2.nome)
conta3 = ContaPoupanca(1212, 254138, 0, cliente3.nome)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

# Cliente 1
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)
# Cliente 2
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)
# Cliente 3
banco.inserir_cliente(cliente3)
banco.inserir_conta(conta3)

# Sistema de autenticação
# Cliente 1
if banco.autenticar(cliente1):
    cliente1.conta.depositar(1000)
    cliente1.conta.sacar(200)
else:
    print(f"{'-=' * 25}")
    print('\033[0;31mCliente não autenticado.\033[m')
    print(f"{'-=' * 25}")
# Cliente 2
if banco.autenticar(cliente2):
    cliente2.conta.depositar(1000)
    cliente2.conta.sacar(200)
else:
    print('\033[0;31mCliente não autenticado.\033[m')
    print(f"{'-=' * 25}")
# Cliente 3
'''A agencia do cliente 3 não faz parte da lista de agencia de autenticação
              somente as agencias [1111, 2222, 3333]'''
if banco.autenticar(cliente3):
    cliente3.conta.depositar(1000)
    cliente3.conta.sacar(200)
else:
    print('\033[0;31mCliente não autenticado.\033[m')
    print(f"{'-=' * 25}")
