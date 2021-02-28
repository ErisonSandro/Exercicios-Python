
lista = []
listapar = []
listaimpar = []

while True:
    num = int(input('Digite um valor: '))
    lista.append(num)

    if num % 2 == 0:
        listapar.append(num)
    else:
        listaimpar.append(num)
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).strip().upper()[0]

    if cont == 'N':
        break

print(f'A lista completa é {lista}')
print(f'A lista de pares é {listapar}')
print(f'A lista de impares é {listaimpar}')