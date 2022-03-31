# Banco Python
 - Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
 - Dicas:
    ---classe que herda (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
    Classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente com limite extra
    Contas têm agência, número da conta, saldo e nome
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
    Banco AGREGANDO classes de clientes e de contas (Agregação)
    Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
 - Só será possível sacar se passar na autenticação do banco (descrita acima)

 
