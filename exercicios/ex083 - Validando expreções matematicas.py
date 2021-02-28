exp = str(input('Digite sua expressão: '))

pee = exp.count('(')
pde = exp.count(')')

if pee == pde:
    print('Expressão valida! ')
else:
    print('Expressão invalida!')

