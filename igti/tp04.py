chute = int(input('Entre com um valor inteiro de 0 a 30: '))
adivinhacao = [5, 6, 10, 14, 16, 20, 30]
if chute in adivinhacao:
    print('Você acertou um dos números que eu estava pensando')
    if chute > 15:
        print('Esse número é maior que 15.')
    if chute < 20:
        print('Esse número é menor que 20')
    print('Você é fera')
else:
    print('Que pena, você errou. Pode tentar outra vez.')
print('Obrigado por participar.')
