cateto_a = 4
endereco = id(cateto_a)

print(endereco)

hexaendereco = hex(endereco)

print(hexaendereco)
a = hex(10914784)
print(a)

b = int('a68be0', 16)
print(b)
print(f'-'*30)

a = 10
b = a
b = 30
print(id(a)==id(b))
print(f'-'*30)

x=1
print(hex(id(x)))
x=x+1
print(hex(id(x)))
print(f'-'*30)

a = 5
print(f'Tipo de a: {type(a)}')

b = 5.0
print(f'Tipo de b: {type(b)}')

c = 2 + 4j
print(f'Tipo de a: {type(c)}')

print(f'Tipo de type: {type(type(c))}')