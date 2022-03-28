from time import sleep


def adicao():
    print('\033[1;32;40mOperação de adição selecionada   \033[m')
    int(input("Digite números inteiros: "))
    soma = contador = 0
    while True:
        numero = int(input("Digite números inteiros: "))
        contador += 1
        soma += numero
        continuar = str(input('\033[0;97;40mDeseja continuar [S/N]? \033[m')).upper()
        if continuar == 'N':
            break
        if continuar != 'S':
            print('\033[0;31mAviso : Opção inválida\033[m')
            print('Digite [S/N]:')
            continuar = str(input('\033[0;97;40mDeseja continuar [S/N]? \033[m')).upper()
            if continuar == 'N':
                break
    print(f"\n\033[1;32;40m   Foram digitados {contador + 1} números   \033[m")
    print(f"\033[1;32;40m   A soma entre eles é: {soma + numero}     \033[m")
    print('\n\033[7;32;40mOperação finalizada com sucesso\033[m\n')
    sleep(0.5)


def subtracao():
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


def multiplicacao():
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


def divisao():
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


def porcentagem():
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


def tabuada():
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


def parimpar():
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


def conversor():
    while True:
        print('\033[1;32;40m   Conversor numérico selecionado   \033[m')
        c = int(input(
            '\033[1;97;40m     Selecione a opção desejada     \033[m\n\033[0;33;40m [1] Binário{:24}\033[m\n\033[0;32;40m [2] Octal{:26}\033[m\n\033[0;34;40m [3] Hexadecimal{:20}\033[m\n '.format(
                '', '', '')))
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
        r = str(input(
            '\033[1;97;40mDeseja realizar outra operação de conversor numérico? [S/N] \033[m')).upper()
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


def cimc():
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
        r = str(
            input('\033[1;97;40mDeseja realizar outra operação de Calculadora IMC? [S/N] \033[m')).upper()
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


def primo():
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
        r = str(input(
            '\033[1;97;40mDeseja realizar outra operação de verificação numero primo? [S/N] \033[m')).upper()
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
