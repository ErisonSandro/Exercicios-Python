#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço
#com 5% de desconto

preço = float(input('Preço do produto? R$'))
desconto = (preço * 5) / 100
total = preço - desconto

print('O valor é {:.2f} e com desconto fica {:.2f}'.format(preço, total))
