def leiadinheiro(msg):
    while True:
        m = str(input(msg)).strip()
        if m.isalpha() or m == '':
            print('Digite uma opção válida!')
        else:
            m = m.replace(',', '.')
            break

    return float(m)
