print('-'*25)
print(' '*5, 'Loja do Nenis')
print('-'*25)
totcompra = maismil = c = menor = 0
prodbarato = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))
    c += 1
    totcompra += preco
    if preco > 1000:
        maismil += 1
    if c == 1:
        menor = preco
        prodbarato = produto
    else:
        if preco < menor:
            menor = preco
            prodbarato = produto
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if cont == 'N':
        break

print(f'O total da compra foi R${totcompra}')
print(f'Temos {maismil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {prodbarato} que custa R${menor}')
