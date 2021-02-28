print('=-'*20)
print('Sequencia de Fibonacci')
print('=-'*20)

num = int(input('Quantos termos voce quer mostrar?'))
t1 = 0
t2 = 1
print('~'*20)
print('{} -> {}'.format(t1, t2), end=' ')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print('-> {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print('Fim')
print('~'*20)
