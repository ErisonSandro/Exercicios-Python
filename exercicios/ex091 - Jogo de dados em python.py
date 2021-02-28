from random import randint
from operator import itemgetter
from time import sleep
cont = 0
jogador = {}

jogador['jogador1'] = randint(1, 6)
jogador['jogador2'] = randint(1, 6)
jogador['jogador3'] = randint(1, 6)
jogador['jogador4'] = randint(1, 6)
ranking = []
print('<<< Valores Sorteados >>>')
for k, v in jogador.items():
    print(f'O {k} tirou {v}')
    sleep(0.3)
print('=-' * 15)
print('   == Ranking dos Jogadores: ==')
ranking = sorted(jogador.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')





