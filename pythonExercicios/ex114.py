import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br')
except:
    print('O site do Pudim NÃO está acessível...')
else:
    print('O site do Pudim está acessível!')