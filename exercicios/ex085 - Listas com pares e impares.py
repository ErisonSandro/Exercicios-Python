lista = [[], []]
valor = 0

for v in range(0, 7):
    num = int(input(f'Digite o {v+1}º valor:'))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

print(f'Os valores pares digitados foram {lista[0]}')



print(f'Os valores impares digitados foram {lista[1]}')

