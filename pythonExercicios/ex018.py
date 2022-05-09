import math

ar = float(input('Digite um ângulo em graus: '))

ag = math.radians(ar)

print('{:.4f}'.format(ag))

sen = math.sin(ar*(math.pi)/180)
cos = math.cos(ar*(math.pi)/180)
tan = math.tan(ar*(math.pi)/180)

print('O ângulo {:.2f}º tem seno igual a {:.3f},'.format(ar, sen), end=' ')
print('cosseno igual a {:.3f} e tangente igual a {:.3f}'.format(cos, tan))
