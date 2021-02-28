nome = str(input('Digite seu nome completo: ')).strip()

primeiro = nome.split()[0]
ultimo = nome.rsplit()[-1]

print('Muito prazer em te conhecer!')
print('Sei primeiro nome é {}'.format(primeiro))
print('Seu ultimo nome é {}'.format(ultimo))
