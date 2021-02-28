lista = []

while True:
    num = int(input('Digite um numero: '))
    lista.append(num)

    cont = ' '
    while cont not in 'SN':
        cont = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break

print('=-'*30)

print(f'Essa lista tem {len(lista)} elementos')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
