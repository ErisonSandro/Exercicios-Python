def area(larg, comp):
    s = larg * comp
    print(f'A area de um terreno ({larg} x {comp}) é de {s}m²')


print('=-' * 20)
print('     Controle de terrenos')
l = float(input('Largura (M): '))
c = float(input('Cumprimento (M): '))
area(l, c)




