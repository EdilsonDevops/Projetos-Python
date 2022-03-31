# Banco Python
 - Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
 - Dicas:<br />
    classe que herda (Herança)<br />
    Pessoa tem nome e idade (com getters)<br />
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)<br />
    Classes ContaPoupanca e ContaCorrente que herdam de Conta<br />
    ContaCorrente com limite extra<br />
    Contas têm agência, número da conta, saldo e nome<br />
    Contas devem ter método para depósito<br />
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)<br />
    Banco AGREGANDO classes de clientes e de contas (Agregação)<br />
    Banco será responsável autenticar o cliente e as contas da seguinte maneira:<br />
    Banco tem contas e clientes (Agregação)<br />
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco'''
 - Só será possível sacar se passar na autenticação do banco (descrita acima)

 
