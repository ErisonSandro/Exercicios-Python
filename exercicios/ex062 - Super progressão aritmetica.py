print('Gerador de PA')
print('-=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{}'.format(termo), end=' - ')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('\nQuantos numeros voce quer mostrar mais ? '))
print('{}'.format(total))
