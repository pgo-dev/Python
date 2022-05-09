def escreva(str):
    str = str.strip()
    print('~'*(len(str)+4))
    print(f'  {str}')
    print('~'*(len(str)+4))

titulo = str(input('Digite a mensagem: '))

escreva(titulo)
