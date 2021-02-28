from random import randint
from time import sleep
lista = []
jogos = []
print('-' * 30)
print('        Jogo Mega Sena           ')
print('-' * 30)
quant = int(input('Quantos jogos voce quer sortear? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1

print('=-' * 5,f'Sorteando {quant} Jogos', '-='*5)
for i, l in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)

print('=-' *5, 'BOA SORTE', '-='*5)