frase = 'Curso em Vídeo Python'

print(frase)
print(frase[3])
print(frase[3:13])
print(frase[13:])
print(frase[1:15])
print(frase[1:15:2])
print(frase[::2])

print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever ot may be) can Pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))

frase2 = '   Curso em Vídeo de Python   '
print(len(frase))
print(len(frase2))
print(len(frase.strip()))

#print(frase.replace('Python',  'Android'))

print(frase.find('Curso'))
print(frase.find('Vídeo'))
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))

dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])
