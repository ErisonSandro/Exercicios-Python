algo = input('Digite algo? ')
valor = algo
print('O tipo primitivo desse valor é ', (type(algo)))
print(valor, 'é uma letra do alfabeto = ', algo.isalpha())
print(valor, 'é um numero = ', algo.isnumeric())
print(valor, 'tem letra e numero = ', algo.isalnum())
print(valor, 'a letra esta maiuscula = ', algo.isupper())
print(valor, 'a letra esta minuscula = ', algo.islower())
print(valor, 'pode ser impresso = ', algo.isprintable())
print(valor, 'é um espaço  = ', algo.isspace())



