# \033[1;97;40m \033[m
# text cor preto:30 vermelho:31 verde:32 amarelo:33 azul:34 magenta:35 ciano:36 cinza:37 branco: 97
# background cor preto:40 vermelho: verde:42 amarelo:33 azul:34 magenta:45 ciano:36 cinza:37 branco 107
print('\033[1;33;40mBem vindo ao sofftware Brasil!!!\033[m')
m = int(input('\033[1;97;40m     Selecione um módulo        \033[m \n\033[0;32;40m [1] Módulo de cálculo          \033[m \n\033[0;33;40m [2] Módulo de nome             \033[m \n\033[0;34;40m [3] Módulo de data             \033[m\n '))
# Módulo de cálculo
if m == 1:
    print('\033[0;32;40mBem vindo ao módulo de cálculos\033[m')
    n1 = int(input('\033[1;97;40m  Escolha a operação desejada  \033[m \n\033[0;32;40m [1] Adição                    \033[m\n\033[0;32;40m [2] Subtração                 \033[m '
                   '\n\033[0;32;40m [3] Multiplicação             \033[m \n\033[0;32;40m [4] Divisão                   \033[m\n\033[0;32;40m [5] Porcentagem               \033[m'
                   '\n\033[0;32;40m [6] Tabuada                   \033[m\n\033[0;32;40m [7] Par ou ímpar              \033[m\n '))
    if n1 == 1:
        print('\033[1;97;40mOperação de adição selecionada   \033[m')
        a1 = int(input('\033[0;97;40mDigite o primeiro número:\033[m'))
        a2 = int(input('\033[0;97;40mDigite o segundo número: \033[m'))
        print('\033[1;32;40m        {} + {} = {}              \033[m'.format(a1, a2, a1 + a2))
        print('\033[7;32;40mOperação finalizada com sucesso...\033[m')
    if n1 == 2:
        print('\033[1;97;40mOperação de subtração selecionada \033[m')
        a1 = int(input('\033[0;97;40mDigite o primeiro número: \033[m'))
        a2 = int(input('\033[0;97;40mDigite o segundo número:  \033[m '))
        print('\033[1;32;40m         {} - {} = {}             \033[m '.format(a1, a2, a1 - a2))
        print('\033[7;32;40mOperação finalizada com sucesso...\033[m')
    if n1 == 3:
        print('\033[1;97;40mOperação de multiplicação selecionada\033[m')
        a1 = int(input('\033[0;97;40mDigite o primeiro número: \033[m'))
        a2 = int(input('\033[0;97;40mDigite o segundo número:  \033[m'))
        print('\033[1;32;40m           {} x {} = {}            \033[m'.format(a1, a2, a1 * a2))
        print('\033[7;32;40mOperação finalizada com sucesso...\033[m')
    if n1 == 4:
        print('\033[1;97;40mOperação de divisão selecionada   \033[m')
        a1 = int(input('\033[0;97;40mDigite o primeiro número: \033[m'))
        a2 = int(input('\033[0;97;40mDigite o segundo número:  \033[m'))
        print('\033[1;32;40m         {} / {} = {}           \033[m'.format(a1, a2, a1 / a2))
        print('\033[7;32;40mOperação finalizada com sucesso...\033[m')
    if n1 == 5:
        print('\033[1;97;40mOperação de porcentagem selecionada\033[m')
        p1 = int(input('\033[0;97;40mInforme a porcetagem: \033[m'))
        p2 = int(input('\033[0;97;40mIforme o número:      \033[m'))
        print('\033[1;32;40m         {}% de {} = {:.0f}          \033[m'.format(p1, p2, p2 * p1 / 100))
        print('\033[7;32;40mOperação finalizada com sucesso...\033[m')
    if n1 == 6:
        print('\033[1;97;40mOperação de tabuada selecionada          \033[m')
        n = int(input('\033[1;97;40mDigite um número para ver na tabuada:  \033[m'))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 1, n * 1))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 2, n * 2))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 3, n * 3))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 4, n * 4))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 5, n * 5))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 6, n * 6))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 7, n * 7))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 8, n * 8))
        print('\033[1;32;40m              {} x {:2} = {}               \033[m'.format(n, 9, n * 9))
        print('\033[1;32;40m              {} x {:2} = {}              \033[m'.format(n, 10, n * 10))
        print('\033[7;32;40m   Operação finalizada com sucesso...    \033[m')
    if n1 == 7:
        print('\033[1;97;40mOperação de verificação de par ou ímpar selecionada\033[m')
        print('\033[0;97;40mDescubra se um número é par ou ímpar               \033[m')
        n = int(input("\033[0;97;40m   Informe um número:   \033[m"))
        if n % 2 == 0:
            print("\033[1;32;40m              O número {} é par.                   \033[m".format(n))
        else:
            print("\033[1;32;40m              O número {} é ímpar.                  \033[m".format(n))
        print('\033[7;32;40m      Operação finalizada com sucesso...           \033[m')
# Módulo de nome
if m == 2:
    print('\033[0;33;40mBem vindo ao módulo de letras\033[m')
    n = int(input('\033[1;97;40m     Selecione uma opção     \033[m\n\033[0;33;40m [1] Leitor de nomes         \033[m \n\033[0;33;40m [2] Sorteio de nomes        \033[m\n'))
    if n == 1:
        print('\033[1;97;40m     Opção de leitor de nomes selecionada      \033[m')
        nome = str(input("\033[0;97;40mDigite seu nome completo:     \033[m")).strip()
        print("\033[0;33;40mNome em maiúsculas: {}. \033[m".format(nome.upper()))
        print("\033[0;33;40mNome em minúsculas: {}. \033[m".format(nome.lower()))
        print("\033[0;33;40mLetras ao todo: {}.                            \033[m".format(len(nome) - nome.count(" ")))
        nome = nome.split()
        print('\033[0;33;40mO primeiro nome é "{}" e ele tem {} letras.\033[m'.format(nome[0], len(nome[0])))
        print('\033[0;33;40mO Último nome é {}" e ele tem {} letras.    \033[m'.format(nome[-1], len(nome[0])))
        print('\033[7;33;40m      Operação finalizada com sucesso...       \033[m')
    if n == 2:
        print('\033[1;97;40m              Opção de sorteio de nomes selecionada          \033[m')
        from random import randint
        print('\033[1;97;40m                           Informe 4 nomes:                  \033[m')
        n1 = input('\033[0;33;40mInforme o 1º Nome: \033[m')
        n2 = input('\033[0;33;40mInforme o 2º Nome: \033[m')
        n3 = input('\033[0;33;40mInforme o 3º Nome: \033[m')
        n4 = input('\033[0;33;40mInforme o 4º Nome: \033[m')
        nomes = [n1, n2, n3, n4]
        counter = 0
        num = randint(0, 3)
        for nome in range(len(nomes)):
            if num == nome:
                print("\033[0;33;40mO nome escolhido é {}, foi o {}º nome informado.         \033[m".format(nomes[nome], counter + 1))
            counter += 1
            nomes = [n1, n2, n3, n4]
        print('\033[7;33;40m             Operação finalizada com sucesso...              \033[m')
        #escolhido = choice(nomes) print("O nome escolhido é {}.".format(escolhido))'''
# Módulo data
if m == 3:
    print('\033[1;97;40mBem vindo ao módulo de data \033[m')
    n = int(input('\033[0;97;40m    Selecione uma opção     \033[m\n\033[0;34;40m [1] Ano bissexto           \033[m\n'))
    if n == 1:
        print('\033[1;97;40mOpção de ano bissexto selecionada \033[m')
        print('\033[0;97;40mDescubra se um ano é bissexto:    \033[m')
        num = int(input("\033[0;97;40mInforme um ano:      \033[m"))
        if num % 4 == 0:
            str_num = str(num)
            if str_num[-2:] == "00":
                if num % 400 == 0:
                    print("\033[1;34;40m         {} é bissexto.         \033[m".format(num))
                else:
                    print("\033[1;34;40m         {} não é bissexto.     \033[m".format(num))
            else:
                print("\033[1;34;40m         {} é bissexto.         \033[m".format(num))
        else:
            print("\033[1;34;40m         {} não é bissexto.     \033[m".format(num))
        print('\033[7;34;40mOperação finalizada com sucesso...\033[m')
