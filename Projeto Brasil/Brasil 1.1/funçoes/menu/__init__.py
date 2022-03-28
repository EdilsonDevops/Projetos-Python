def menuprincipal():
    print('\033[1;33;40mBem vindo ao software Brasil!!! \033[m')
    print(
        '\033[1;97;40m{:^32}\033[m \n\033[0;32;40m {:31}\033[m \n\033[0;33;40m {:31}\033[m \n\033[0;34;40m {:31}\033[m\n\033[0;31;40m {:31}\033[m\n'.format(
            'Selecione um módulo', '[1] Módulo de cálculo', '[2] Módulo de letras', '[3] Módulo de data',
            '[4] Encerrar o programa'))


def menucalculos():
    print('\033[0;32;40mBem vindo ao módulo de cálculos\033[m')
    print(
        '\033[1;97;40m  {}\033[m \n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[m\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n\033[0;32;40m {:30}\033[m\n'.format(
            'Escolha a operação desejada  ', '[1] Adição', '[2] Subtração', '[3] Multiplicação', '[4] Divisão',
            '[5] Porcentagem', '[6] Tabuada', '[7] Par ou ímpar', '[8] Conversor numérico',
            '[9] Calculadora IMC',
            '[10] Número primo', '[11] Voltar ao menu'))


def menuletras():
    print('\033[0;33;40mBem vindo ao módulo de letras\033[m')
    print(
        '\033[1;97;40m{:^29}\033[m\n\033[0;33;40m {:28}\033[m \n\033[0;33;40m {:28}\033[m\n\033[0;33;40m {:28}\033[m\n'.format(
            'Selecione uma opção', '[1] Leitor de nomes', '[2] Sorteio de nomes', '[3] Voltar ao menu'))
