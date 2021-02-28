jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    resp = ' '
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        break

print('=-' * 30)
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<20}', end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('=-' * 30)

while True:
    busca = int(input('Quer saber os dados de qual jogador? (999 - stop): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro!, não existe jogador com o codigo {busca}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'    Na partida {i+1} fez {g} gols')
    print('=-' * 30)
print('<<Volte Sempre>>')

