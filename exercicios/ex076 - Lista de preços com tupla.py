listaprod = ('lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
'Compasso', 9.90, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90)
print('=-'*32)
print('{:^55}'.format('LISTAGEM DE PREÇOS'))
print('=-'*32)

for org in listaprod:
    if type(org) is str:
        print(f'{org:_<55}', end='R$')
    else:
        print(f'{org:>6.2f}')