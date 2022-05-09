def titulo(msg):
    msg = msg.strip().upper()
    print('-'*30)
    print(f'{msg:^30}')
    print('-' * 30)

men = str(input('Digite seu título: '))

men = men.strip().upper()

print(titulo(men))
