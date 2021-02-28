#Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua area e quantidade de tinta necessaria para pinta-la,
# sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e sua aréa é de {}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))

