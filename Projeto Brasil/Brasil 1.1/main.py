# \033[1;97;40m \033[m
# text cor preto: 30 vermelho: 31 verde: 32 amarelo: 33 azul: 34 magenta: 35 ciano: 36 cinza: 37 branco: 97
# fundo preto: 40 vermelho: 41 verde: 42 amarelo: 33 azul: 34 magenta: 45 ciano: 36 cinza: 37 branco 107
from funçoes import menu, calculos, letras, data
menu.menuprincipal()  # Função menu
m = int(input("\033[1:97:40mSelecione o módulo desejado de 1 a 3: \033[m"))
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
            menu.menucalculos()
            n1 = int(input("\033[1:97:40mSelecione a opção desejada de 1 a 10: \033[m"))
            # Adição
            if n1 == 1:
                calculos.adicao()
            # Subtração
            elif n1 == 2:
                calculos.subtracao()
            # Multiplicação
            elif n1 == 3:
                calculos.multiplicacao()
            # Divisão
            elif n1 == 4:
                calculos.divisao()
            # Porcentagem
            elif n1 == 5:
                calculos.porcentagem()
            # Tabuada
            elif n1 == 6:
                calculos.tabuada()
            # Par ou ímpar
            elif n1 == 7:
                calculos.parimpar()
            # Conversor numérico
            elif n1 == 8:
                calculos.conversor()
            # Calculadora IMC
            elif n1 == 9:
                calculos.cimc()
            # Número primo
            elif n1 == 10:
                calculos.primo()
            elif n1 > 11:  # exceção maior
                print("\033[0;33mAviso: escolha um número de 1 a 11.\033[m")
            elif n1 < 0:  # exceção menor
                print("\033[0;33mAviso: escolha um número positivo.\033[m")
            elif n1 == 0:  # exceção zero
                print("\033[0;33mAviso: escolha um número de 1 a 11.\033[m")
            else:
                menu.menuprincipal()
                m = int(input("\033[1:97:40mSelecione o módulo desejado de 1 a 3:\033[m \n"))
        # Módulo de letras
        elif m == 2:
            menu.menuletras()
            n = int(input("\033[1:97:40mSelecione a opção desejada de 1 a 2: \033[m"))
            # Leitor de letras
            if n == 1:
                letras.leitor()
            # sorteio
            elif n == 2:
                letras.sorteio()
            elif n > 3:  # exceção maior
                print("\033[0;33mAviso: escolha um número de 1 a 3.\033[m")
            elif n < 0:  # exceção menor
                print("\033[0;33mAviso: escolha um número positivo.\033[m")
            elif n == 0:  # exceção zero
                print("\033[0;33mAviso: escolha um número de 1 a 3.\033[m")
            else:
                menu.menuprincipal()
                m = int(input("\033[1:97:40mSelecione o módulo desejado de 1 a 3: \033[m"))
        # Módulo de data
        elif m == 3:
            print('\033[1;34;40mBem vindo ao módulo de data \033[m')
            n = int(input(
                '\033[0;97;40m{:^28}\033[m\n\033[0;34;40m {:27}\033[m\n\033[0;34;40m {:27}\033[m\n'.format(
                    'Selecione uma opção',
                    '[1] Ano bissexto', '[2] Voltar ao menu')))
            # ano
            if n == 1:
                data.ano()
            elif n > 2:  # exceção maior
                print("\033[0;33mAviso: escolha um número de 1 a 2.\033[m")
            elif n < 0:  # exceção menor
                print("\033[0;33mAviso: escolha um número positivo.\033[m")
            elif n == 0:  # exceção zero
                print("\033[0;33mAviso: escolha um número de 1 a 2.\033[m")
            else:
                menu.menuprincipal()
                m = int(input("\033[1:97:40mSelecione o módulo desejado de 1 a 3:\033[m \n"))
print("\033[1;31;40mOpção 4: programa encerrado.\033[m")
