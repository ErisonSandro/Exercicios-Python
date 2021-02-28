from math import hypot

oposto = float(input('cumprimento do cateto oposto: '))
adjacente = float(input('cumprimento do cateto adjacente: '))


print('A hipotenusa vai medir {:.2f}'.format(hypot(oposto, adjacente)))


