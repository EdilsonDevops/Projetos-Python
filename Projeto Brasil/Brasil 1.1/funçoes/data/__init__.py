from time import sleep


def ano():
    while True:
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
