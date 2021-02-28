# Escreva um programa que leia um valor em metros e o exiba convertido
# em centimentros e milimetros

num = float(input('Uma distancia em metros: '))
km = num / 1000
hm = num / 100
dam = num / 10
dm = num * 10
cm = num * 100
mm = num * 1000



print('a medida de {} corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(num, km, hm, dam, dm, cm, mm))

