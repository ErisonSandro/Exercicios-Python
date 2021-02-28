#crie um algoritmo que leia um numero e mostro o seu
# dobro, triplo e a raiz quadrada.

num = int(input('Digite um numero: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)

print('seu numero é {} \no dobro é {} \no triplo é {} \na raiz quadrada é {:.2f}'.format(num, dobro, triplo, raiz))


