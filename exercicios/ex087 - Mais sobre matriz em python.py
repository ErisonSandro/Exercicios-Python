matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

par = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor na posição [{l} - {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]




    print()


print('=-' * 20)



print(f'A soma dos valores pares é {par}')

print(f'A soma dos valores da terceira coluna é {matriz[0][2]+matriz[1][2]+matriz[2][2]}')



print(f'O maior valor da segunda linha é {max(matriz[1])}')

