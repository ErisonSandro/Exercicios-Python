print('=-'*15)
print('10 TERMOS DE UMA PA')
print('=-'*15)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razão

for c in range(primeiro, decimo+razão, razão):
    print('{}'.format(c), end=' - ')
print('Acabou')