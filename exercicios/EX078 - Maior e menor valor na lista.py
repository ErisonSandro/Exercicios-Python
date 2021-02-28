valores = []
maior = menor = 0

for c, v in enumerate(range(0, 5)):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))


print('=-'*20)

print(f'Voce digitou os valores {valores}')


print(f'O maior valor digitado foi {max(valores)} na posição ', end='')
for i, z in enumerate(valores):
    if z == max(valores):
        print(f'{i}..', end=' ')

print(f'\nO menor valor digitado foi {min(valores)} na posição ', end='')
for i, z in enumerate(valores):
    if z == min(valores):
        print(f'{i}..', end=' ')

