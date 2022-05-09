def contador(i, f , p):
    '''
    Faz uma contagem e mostra na tela
    :param i: valor de início da contagem
    :param f: valor de fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    '''
    c = i
    while c<= f:
        print(f'{c} ', end='')
        c = c + p
    print(' FIM!')

help(contador)
