import random
import time

nu = int(input('Digite um número de 0 a 5: '))

nc = random.randint(0, 5)

print('PROCESSANDO...')
time.sleep(2)

print('O número sorteado é: {}'.format(nc))

if nu == nc:
    print('Parabéns, você acertou!')
else:
    print('Você errou.')