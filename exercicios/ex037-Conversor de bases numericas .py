num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para conversão: \n[1] converter para BINARIO \n[2] converter para OCTA \n[3] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))



if opcao == 1:
    print('{} convertidos para BINARIO é igual a {}'.format(num, bin(num) [2:]))

elif opcao == 2:
    print('{} convertidos para OCTAL é igual a {}'.format(num, oct(num)[2:]))

elif opcao == 3:
   print('{} convertidos para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))

else:
    print('Opção invalida. Tente novamente')
