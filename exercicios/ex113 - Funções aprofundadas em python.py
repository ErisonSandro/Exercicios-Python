def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um numero inteiro!\033[m')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuario! ')

        return n



def leiareal(txt):
    while True:
        try:
            r = float(input(txt))
        except(ValueError, TypeError):
            print('\033[31mErro!, Por favor digite um numero real valido!\033[m')
        except KeyboardInterrupt:
            print('Entrada de dados cancelada pelo usuario!')
        else:
            return r




num = leiaint('Digite um valor inteiro: ')
nr = leiareal('Digite um numero real: ')
print(f'O valor inteiro digitado foi {num}')
print(f'O valor real digitado foi {nr}')




