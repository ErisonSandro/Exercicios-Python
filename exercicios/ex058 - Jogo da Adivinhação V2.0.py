#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import time
import random
print('-=-'*20)
print('SOU SEU COMPUTADOR...')
print('Acabei de pensar em um numero entre 0 e 10')
print('Será que voce consegue adivinhar?')
print('-=-'*20)

cont = 0
numero = 0
pc = random.randint(0, 10)
while numero != pc:
    numero = int(input('Qual é o seu palpite? '))
    cont += 1
    if numero == pc:
        print('Parabens voce acertou')
        print('Acertou com {} tentativas'.format(cont))
    else:
        if numero < pc:
            print('Mais.. Tente mais uma vez')
        if numero > pc:
            print('Menos.. Tente mais uma vez')

