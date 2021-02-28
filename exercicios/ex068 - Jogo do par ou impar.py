from random import randint
cont = 0
print('=-'*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o computador {computador}. Total de {total} ', end='')
    print('Deu Par' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('<>' * 15)
            print('Voce Venceu!')
            print('<>' * 15)

            cont += 1
            print('Vamos Jogar Novamente! ...')
        else:
            print('<>' * 15)
            print('Voce Perdeu')
            print('<>' * 15)
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('<>' * 15)
            print('Voce venceu')
            cont += 1
            print('Vamos Jogar Novamente! ...')

        else:
            print('<>' * 15)
            print('Voce perdeu!')
            print('<>' * 15)
            break
print(f'Game Over! Voce venceu {cont} vezes.')
