while True:
    t = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'quatorze',
         'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')

    while True:
        n = int(input('Digite um número entre zero a vinte: '))
        if 0 <= n <= 20:
            break
        else:
            print('Tente novamente!')


    print(t[n])