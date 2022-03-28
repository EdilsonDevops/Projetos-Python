from time import sleep


def leitor():
    while True:
        print('\033[1;33;40m{:^47}\033[m'.format('Opção de leitor de nomes selecionada'))
        nome = str(input("\033[0;97;40mDigite seu nome completo:     \033[m")).strip()
        print(f"\n\033[0;33;40mNome em maiúsculas: {nome.upper()}. \033[m")
        print(f"\033[0;33;40mNome em minúsculas: {nome.lower()}. \033[m")
        print("\033[0;33;40mLetras ao todo: {}.{:28}\033[m".format(len(nome) - nome.count(" "), ' '))
        nome = nome.split()
        print(f'\033[0;33;40mO primeiro nome é "{nome[0]}" e ele tem {len(nome[0])} letras.\033[m')
        print(f'\033[0;33;40mO Último nome é {nome[-1]}" e ele tem {len(nome[0])} letras.    \033[m\n')
        r = str(
            input('\033[1;97;40mDeseja realizar outra operação de leitor de nomes? [S/N] \033[m')).upper()
        if r == 'N':
            break
        elif r != 'S':
            print('\033[0;31mAviso : Opção inválida\033[m')
            print('Digite [S/N]:')
            r = str(input('Deseja continuar [S/N]? ')).upper()
            if r == 'N':
                break
    print(f"\033[7;33;40m{'Operação finalizada com sucesso...':^47}\033[m\n")
    sleep(0.5)


def sorteio():
    while True:
        print('\033[1;33;40m{:^61}\033[m'.format('Opção de sorteio de nomes selecionada'))
        from random import randint
        print('\033[1;97;40m{:^61}\033[m'.format('Informe 4 nomes:'))
        n1 = input('\033[0;97;40mInforme o 1º Nome: \033[m')
        n2 = input('\033[0;97;40mInforme o 2º Nome: \033[m')
        n3 = input('\033[0;97;40mInforme o 3º Nome: \033[m')
        n4 = input('\033[0;97;40mInforme o 4º Nome: \033[m')
        nomes = [n1, n2, n3, n4]
        counter = 0
        num = randint(0, 3)
        for nome in range(len(nomes)):
            if num == nome:
                print(
                    f"\n\033[0;33;40m O nome escolhido é {nomes[nome]}, foi o {counter + 1}º nome informado.        \033[m\n")
            counter += 1
            nomes = [n1, n2, n3, n4]
        r = str(
            input('\033[1;97;40m Deseja realizar outra operação de sorteio de nomes? [S/N] \033[m')).upper()
        if r == 'N':
            break
        elif r != 'S':
            print('\033[0;31mAviso : Opção inválida\033[m')
            print('Digite [S/N]:')
            r = str(input('Deseja continuar [S/N]? ')).upper()
            if r == 'N':
                break
    print(f"\033[7;33;40m{'Operação finalizada com sucesso...':^61}\033[m\n")
    sleep(0.5)
    # escolhido = choice(nomes) print("O nome escolhido é {}.".format(escolhido))
