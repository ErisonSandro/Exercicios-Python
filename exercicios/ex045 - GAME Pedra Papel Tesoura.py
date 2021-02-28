from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
print('Suas opções: ')
print('[0] PEDRA\n[1] PAPEL\n[2] TESOURA')
jogador = int(input('Qual sua jogada? '))
computador = randint(0, 2)

if jogador > 2:
    print('JOGADA INVALIDA')
else:
    sleep(0.5), print('JO')
    sleep(0.8), print('KEN')
    sleep(1), print('PO!!')
    sleep(0.5)

    print('=-' * 20)
    print('COMPUTADOR = {}'.format(itens[computador]))
    print('JOGADOR = {}'.format(itens[jogador]))
    print('=-' * 20)

    if computador == 0:
        if jogador == 0:
            print('EMPATOU')
        elif jogador == 1:
            print('JOGADOR VENCE')
        elif jogador == 2:
            print('COMPUTADOR')
        else:
            print('JOGADA INVALIDA')

    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCE')
        elif jogador == 1:
            print('EMPATOU')
        elif jogador == 2:
            print('JOGADOR VENCE')
        else:
            print('JOGADA INVALIDA')
    elif computador == 2:
        if jogador == 0:
            print('JOGADOR VENCE')
        elif jogador == 1:
            print('COMPUTADOR VENCE')
        elif jogador == 2:
            print('EMPATOU')
        else:
            print('JOGADA INVALIDA')
