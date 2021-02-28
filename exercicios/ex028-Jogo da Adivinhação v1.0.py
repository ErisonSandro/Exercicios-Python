import time
import random
print('-=-'*30)
print('Vou pensar em um numero entre 0 e 5. tente adivinhar...')
print('-=-'*30)
numero = int(input('Em que numero pensei? '))
pc = random.randint(0, 5)

print('Processando...')
time.sleep(1)

if numero == pc:
    print('Voce acertou! Parabens')
else:
    print('Ganhei! Eu pensei no numero {} e não no {}'.format(pc, numero))

