num = int(input('Digite um numero para calcular seu fatorial: '))

cont = num
fatorial = 1
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print(fatorial)


