# \033[1;97;40m \033[m
# text cor preto: 30 vermelho: 31 verde: 32 amarelo: 33 azul: 34 magenta: 35 ciano: 36 cinza: 37 branco: 97
# fundo preto: 40 vermelho: verde:42 amarelo:33 azul: 34 magenta: 45 ciano: 36 cinza: 37 branco 107

print('\033[1;33;40mBem vindo ao software Brasil!!! \033[m')
print(
    '\033[1;97;40m{:^32}\033[m \n\033[0;32;40m {:31}\033[m \n\033[0;33;40m {:31}\033[m \n\033[0;34;40m {:31}\033[m\n\033[0;31;40m {:31}\033[m\n'.format(
        'Selecione um módulo', '[1] Módulo de cálculo', '[2] Módulo de nome', '[3] Módulo de data',
        '[4] Encerrar o programa'))
m = int(input("\033[1:97:40mSelecione o módulo desejado de 1 a 3:\033[m \n"))
while m != 4:
    if m > 4:  # exceção maior
        print("Aviso: escolha um número de 1 a 4.")
        m = int(input("Sua escolha: \n"))
    elif m < 0:  # exceção menor
        print("Aviso: escolha um número positivo.")
        m = int(input("Sua escolha: \n"))
    else:  # Iniciamento do programa:
        # Módulo de cálculo
        if m == 1:
            from time import sleep
            print('\033[0;32;40mBem vindo ao módulo de cálculos\033[m')
            n1 = int(input(
                '\033[1;97;40m  {}\033[m \n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[m\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n'.format(
                    'Escolha a operação desejada  ', '[1] Adição', '[2] Subtração', '[3] Multiplicação', '[4] Divisão',
                    '[5] Porcentagem', '[6] Tabuada', '[7] Par ou ímpar', '[8] Conversor numérico',
                    '[9] Calculadora IMC',
                    '[10] Número primo', '[11] Voltar ao menu')))
            # Adição
            if n1 == 1:
                print('\033[1;32;40mOperação de adição selecionada   \033[m')
                a = int(input("Digite números inteiros: "))
                soma = contador = 0
                while True:
                    n = int(input("Digite números inteiros: "))
                    contador += 1
                    soma += n
                    p = str(input('\033[0;97;40mDeseja continuar [S/N]? \033[m')).upper()
                    if p == 'N':
                        break
                    if p != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        p = str(input('\033[0;97;40mDeseja continuar [S/N]? \033[m')).upper()
                        if p == 'N':
                            break
                print(f"\n\033[1;32;40m   Foram digitados {contador+1} números   \033[m")
                print(f"\033[1;32;40m   A soma entre eles é: {soma+a}     \033[m")
                print('\n\033[7;32;40mOperação finalizada com sucesso\033[m\n')
                sleep(0.5)
            # Subtração
            elif n1 == 2:
                while True:
                    print('\033[1;32;40mOperação de subtração selecionada \033[m')
                    n1 = int(input('\033[0;97;40mDigite o primeiro número: \033[m'))
                    n2 = int(input('\033[0;97;40mDigite o segundo número:  \033[m'))
                    print(f"\n\033[1;32;40m{' ':11}{n1} - {n2} = {n1 - n2}{' ':12}\033[m \n")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de subtração? [S/N]\033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        p = str(input('\033[1;97;40mDeseja continuar [S/N]? \033[m')).upper()
                        if p == 'N':
                            break
                print('\033[7;32;40mOperação finalizada com sucesso...\033[m \n')
                sleep(0.5)
            # Multiplicação
            elif n1 == 3:
                while True:
                    print('\033[1;32;40mOperação de multiplicação selecionada\033[m')
                    n1 = int(input('\033[0;97;40mDigite o primeiro número: \033[m'))
                    n2 = int(input('\033[0;97;40mDigite o segundo número:  \033[m'))
                    print(f"\n\033[1;32;40m{' ':10}{n1} x {n2} = {n1 * n2}{' ':11}\033[m\n")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de multiplicação? [S/N] \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;32;40mOperação finalizada com sucesso...\033[m\n')
                sleep(0.5)
            # Divisão
            elif n1 == 4:
                while True:
                    print('\033[0;32;40mOperação de divisão selecionada   \033[m')
                    a1 = int(input('\033[0;97;40mDigite o primeiro número: \033[m'))
                    a2 = int(input('\033[0;97;40mDigite o segundo número:  \033[m'))
                    print(f"\n\033[1;32;40m{' ':10}{a1} / {a2} = {a1 / a2:.0f}{' ':11}\033[m\n")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de divisão? [S/N] \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;32;40mOperação finalizada com sucesso...\033[m\n')
                sleep(0.5)
            # Porcentagem
            elif n1 == 5:
                while True:
                    print('\033[1;32;40mOperação de porcentagem selecionada\033[m')
                    n1 = int(input('\033[0;97;40mInforme a porcentagem: \033[m'))
                    n2 = int(input('\033[0;97;40mInforme o número:      \033[m'))
                    print(f"\n\033[1;32;40m{' ':9}{n1}% de {n2} = {n2 * n1 / 100:.0f}{' ':10}\033[m\n")
                    r = str(input('\033[1;97;40mDeseja realizar outra Operação de porcentagem? [S/N] \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;32;40mOperação finalizada com sucesso...\033[m\n')
                sleep(0.5)
            # Tabuada
            elif n1 == 6:
                while True:
                    print('\033[1;32;40mOperação de tabuada selecionada\033[m')
                    n = int(input("\033[1;97;40mQual tabuada você deseja?: \033[m"))
                    for i in range(1, 11):
                        print(f"\033[1;32;40m       {n} x {i} = {n * i}        \033[m")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de tabuada? [S/N] \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;32;40m   Operação finalizada com sucesso...    \033[m\n')
                sleep(0.5)
            # Par ou ímpar
            elif n1 == 7:
                while True:
                    print('\033[1;32;40mOperação de verificação de par ou ímpar selecionada\033[m')
                    print('\033[0;97;40mDescubra se um número é par ou ímpar               \033[m')
                    n = int(input("\033[0;97;40m   Informe um número:   \033[m"))
                    if n % 2 == 0:
                        print(f"\n\033[1;32;40m{' ':16}O número {n} é par.{' ':17}\033[m\n")
                    else:
                        print(f"\n\033[1;32;40m{' ':15}O número {n} é ímpar.{' ':16}\033[m\n")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de par ou ímpar? [S/N] \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;32;40mOperação finalizada com sucesso...\033[m\n')
                sleep(0.5)
            # Conversor numérico
            elif n1 == 8:
                while True:
                    print('\033[1;32;40m   Conversor numérico selecionado   \033[m')
                    c = int(input('\033[1;97;40m     Selecione a opção desejada     \033[m\n\033[0;33;40m [1] Binário{:24}\033[m\n\033[0;32;40m [2] Octal{:26}\033[m\n\033[0;34;40m [3] Hexadecimal{:20}\033[m\n '.format('', '', '')))
                    if c == 1:
                        print("\033[1;33;40m  Você escolheu o conversor binário.  \033[m")
                        b = int(input('\033[0;97;40mInforme um número para a conversão: \033[m'))
                        print(f"\n\033[1;33;40m  {b} convertido para binário é: {bin(b)[2:]}.  \033[m\n")
                    elif c == 2:
                        print("\033[1;32;40m        Você escolheu octal.        \033[m")
                        o = int(input('\033[0;97;40mInforme um número para a conversão: \033[m'))
                        print(f"\n\033[1;32;40m   {o} convertido para octal é: {oct(o)[2:]}.  \033[m\n")
                    elif c == 3:
                        print("\033[1;34;40m     Você escolheu hexadecimal.     \033[m")
                        h = int(input('\033[0;97;40mInforme um número para a conversão: \033[m'))
                        print(f"\033[1;34;40m  {h} convertido para hexadecimal é: {hex(h)[2:].upper()}.  \033[m")
                    else:
                        print("Por favor, escolha apenas uma das 3 opções.")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de conversor numérico? [S/N] \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;32;40mOperação finalizada com sucesso...\033[m\n')
                sleep(0.5)
            # Calculadora IMC
            elif n1 == 9:
                while True:
                    print('\033[1;32;40m  Calculadora IMC selecionada  \033[m')
                    peso = float(input("\033[0;97;40mDigite seu peso (em kg):  \033[m"))
                    altura = float(input("\033[0;97;40mDigite sua altura (em m): \033[m"))
                    imc = (peso / (altura ** 2))
                    if imc < 18.5:
                        print(f"\n\033[1;32;40m  Seu IMC é de: {imc:.1f}. Você está abaixo do peso.  \033[m\n")
                    elif imc < 25:
                        print(f"\n\033[1;32;40m  Seu IMC é de: {imc:.1f}. Você está no peso ideal.  \033[m\n")
                    elif imc < 30:
                        print(f"\n\033[1;32;40m  Seu IMC é de: {imc:.1f}. Você está com sobrepeso.  \033[m\n")
                    elif imc < 40:
                        print(f"\n\033[1;32;40m  Seu IMC é de : {imc:.1f}. Você está com obesidade.  \033[m\n")
                    else:
                        print(f"\n\033[1;32;40m  Seu IMC é de {imc:.1f}. Você está com obesidade mórbida.  \033[m\n")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de Calculadora IMC? [S/N] \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;32;40mOperação finalizada com sucesso...\033[m\n')
                sleep(0.5)
            # Número primo
            elif n1 == 10:
                while True:
                    print('\033[1;32;40mDescubra se um número é primo\033[m')
                    num = int(input("Informe um número: "))
                    isPrime = True
                    current = (num // 2)
                    for i in range(current, 0, -1):
                        if num % i == 0 and i != 1:
                            isPrime = False
                    if isPrime:
                        print(f"\n\033[1;32;40mO número {num} é primo.\033[m\n")
                    else:
                        print(f"\n\033[1;32;40mO número {num} não é primo.\033[m\n")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de verificação numero primo? [S/N] \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;32;40mOperação finalizada com sucesso...\033[m\n')
                sleep(0.5)
            elif n1 > 11:  # exceção maior
                print("\033[0;33mAviso: escolha um número de 1 a 11.\033[m")
            elif n1 < 0:  # exceção menor
                print("\033[0;33mAviso: escolha um número positivo.\033[m")
            elif n1 == 0:  # exceção zero
                print("\033[0;33mAviso: escolha um número de 1 a 11.\033[m")
            else:
                print('\033[1;33;40mBem vindo ao software Brasil!!!\033[m')
                print(
                    '\033[1;97;40m{:^32}\033[m \n\033[0;32;40m {:31}\033[m \n\033[0;33;40m {:31}\033[m \n\033[0;34;40m {:31}\033[m\n\033[0;31;40m {:31}\033[m\n'.format(
                        'Selecione um módulo', '[1] Módulo de cálculo', '[2] Módulo de nome', '[3] Módulo de data',
                        '[4] Encerrar o programa'))
                m = int(input("\033[1:97:40mSelecione o módulo desejado de 1 a 3:\033[m \n"))
        # Módulo de nome
        elif m == 2:
            from time import sleep
            print('\033[0;33;40mBem vindo ao módulo de letras\033[m')
            n = int(input(
                '\033[1;97;40m{:^29}\033[m\n\033[0;33;40m {:28}\033[m \n\033[0;33;40m {:28}\033[m\n\033[0;33;40m {:28}\033[m\n'.format(
                    'Selecione uma opção', '[1] Leitor de nomes', '[2] Sorteio de nomes', '[3] Voltar ao menu')))
            if n == 1:
                while True:
                    print('\033[1;33;40m{:^47}\033[m'.format('Opção de leitor de nomes selecionada'))
                    nome = str(input("\033[0;97;40mDigite seu nome completo:     \033[m")).strip()
                    print(f"\n\033[0;33;40mNome em maiúsculas: {nome.upper()}. \033[m")
                    print(f"\033[0;33;40mNome em minúsculas: {nome.lower()}. \033[m")
                    print("\033[0;33;40mLetras ao todo: {}.{:28}\033[m".format(len(nome) - nome.count(" "), ' '))
                    nome = nome.split()
                    print(f'\033[0;33;40mO primeiro nome é "{nome[0]}" e ele tem {len(nome[0])} letras.\033[m')
                    print(f'\033[0;33;40mO Último nome é {nome[-1]}" e ele tem { len(nome[0])} letras.    \033[m\n')
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de leitor de nomes? [S/N] \033[m')).upper()
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
            elif n == 2:
                from time import sleep
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
                            print(f"\n\033[0;33;40m O nome escolhido é {nomes[nome]}, foi o {counter + 1}º nome informado.        \033[m\n")
                        counter += 1
                        nomes = [n1, n2, n3, n4]
                    r = str(input('\033[1;97;40m Deseja realizar outra operação de sorteio de nomes? [S/N] \033[m')).upper()
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
            elif n > 3:  # exceção maior
                print("\033[0;33mAviso: escolha um número de 1 a 3.\033[m")
            elif n < 0:  # exceção menor
                print("\033[0;33mAviso: escolha um número positivo.\033[m")
            elif n == 0:  # exceção zero
                print("\033[0;33mAviso: escolha um número de 1 a 3.\033[m")
            else:
                print('\033[1;33;40mBem vindo ao software Brasil!!!\033[m')
                print(
                    '\033[1;97;40m{:^32}\033[m \n\033[0;32;40m {:31}\033[m \n\033[0;33;40m {:31}\033[m \n\033[0;34;40m {:31}\033[m\n\033[0;31;40m {:31}\033[m\n'.format(
                        'Selecione um módulo', '[1] Módulo de cálculo', '[2] Módulo de nome', '[3] Módulo de data',
                        '[4] Encerrar o programa'))
                m = int(input("\033[1:97:40mSelecione o módulo desejado de 1 a 3:\033[m \n"))
        # Módulo de data
        elif m == 3:
            print('\033[1;34;40mBem vindo ao módulo de data \033[m')
            n = int(input(
                '\033[0;97;40m{:^28}\033[m\n\033[0;34;40m {:27}\033[m\n\033[0;34;40m {:27}\033[m\n'.format(
                    'Selecione uma opção',
                    '[1] Ano bissexto', '[2] Voltar ao menu')))
            if n == 1:
                while True:
                    from time import sleep
                    print('\033[1;34;40mOpção de ano bissexto selecionada \033[m')
                    print('\033[0;97;40mDescubra se um ano é bissexto:    \033[m')
                    num = int(input("\033[0;97;40mInforme um ano:      \033[m"))
                    if num % 4 == 0:
                        str_num = str(num)
                        if str_num[-2:] == "00":
                            if num % 400 == 0:
                                print(f"\n\033[1;34;40m         {num} é bissexto.         \033[m\n")
                            else:
                                print(f"\n\033[1;34;40m         {num} não é bissexto.     \033[m\n")
                        else:
                            print(f"\n\033[1;34;40m         {num} é bissexto.         \033[m\n")
                    else:
                        print(f"\n\033[1;34;40m         {num} não é bissexto.     \033[m\n")
                    r = str(input('\033[1;97;40mDeseja realizar outra operação de ano bissexto? [S/N]  \033[m')).upper()
                    if r == 'N':
                        break
                    elif r != 'S':
                        print('\033[0;31mAviso : Opção inválida\033[m')
                        print('Digite [S/N]:')
                        r = str(input('Deseja continuar [S/N]? ')).upper()
                        if r == 'N':
                            break
                print('\033[7;34;40mOperação finalizada com sucesso...\033[m\n')
                sleep(0.5)
            elif n > 2:  # exceção maior
                print("\033[0;33mAviso: escolha um número de 1 a 2.\033[m")
            elif n < 0:  # exceção menor
                print("\033[0;33mAviso: escolha um número positivo.\033[m")
            elif n == 0:  # exceção zero
                print("\033[0;33mAviso: escolha um número de 1 a 2.\033[m")
            else:
                print('\033[1;33;40mBem vindo ao software Brasil!!!\033[m')
                print(
                    '\033[1;97;40m{:^32}\033[m \n\033[0;32;40m {:31}\033[m \n\033[0;33;40m {:31}\033[m \n\033[0;34;40m {:31}\033[m\n\033[0;31;40m {:31}\033[m\n'.format(
                        'Selecione um módulo', '[1] Módulo de cálculo', '[2] Módulo de nome', '[3] Módulo de data',
                        '[4] Encerrar o programa'))
                m = int(input("\033[1:97:40mSelecione o módulo desejado de 1 a 3:\033[m \n"))
print("\033[1;31;40mOpção 4: programa encerrado.\033[m")
