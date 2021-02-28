totgols = 0
jogador = {}
gols = []
jogador['Nome'] = str(input('Nome do jogador: '))
totpartidas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, totpartidas):
    jogador['gols'] = int(input(f'  Quantos gols na partida {c}?'))
    totgols += jogador['gols']
    gols.append(jogador['gols'])
    jogador['gols'] = gols[:]

jogador['total'] = totgols

print('=-' * 30)
print(jogador)
print('=-' * 30)

for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')
print('=-' * 30)

print(f'O jogador {jogador["Nome"]} jogou {len(jogador["gols"])} partidas')
for c, i in enumerate(jogador['gols']):
    print(f'  > Na partida {c}, fez {i} gols')
print(f'Foi um total de {totgols} gols')