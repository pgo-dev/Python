cidade = str(input('Digite um nome de uma cidade: ')).strip()

cidade = cidade.lower().find('santo')
print(cidade)

if cidade == 0:
   print('Possui Santo no início')
else:
    print('Não possui Santo no início')
