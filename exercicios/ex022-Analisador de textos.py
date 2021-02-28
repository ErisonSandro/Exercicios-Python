nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome...')
print('Seu nome em maiusculas é ', nome.upper())
print('Seu nome em minusculas é ', nome.lower())
dividido = nome.split()
print('Sei nome ao todo tem {} letras'.format(len(nome.replace(' ','')))) #print(len(nome) - nome.count(' '))
cont = len(dividido[0])
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0], cont))

