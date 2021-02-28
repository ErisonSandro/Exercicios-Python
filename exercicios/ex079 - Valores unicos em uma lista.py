valores = list()

while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Não vou adicionar o numero ja existe')

    cont = ' '
    while cont not in 'NS':
        cont = str(input('Quer continuar [S/N]: ')).upper().strip()
    if cont == 'N':
        break
print('=-'*30)
valores.sort()
print(f'voce digitou os valores {valores}')



