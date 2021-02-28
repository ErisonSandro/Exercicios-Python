from time import sleep
c = ['\033[m',          # 0 SEM COR
     '\033[0;30;41m',   # 1 VERMELHO
     '\033[0;30;42m',   # 2 VERDE
     '\033[0;30;44m',   # 3 AZUL
     '\033[7;40m',    # 4 BRANCO
     ]

def ajuda(v):
    titulo(f'Acessando o manual do comando \'{v}\'', 3)
    print(c[4], end='')
    help(v)
    print(c[2], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam,)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Ate logo!', 1)