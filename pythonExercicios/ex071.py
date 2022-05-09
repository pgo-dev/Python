cont50 = cont20 = cont10 = cont1 = 0
c = 1
v = float(input('Quanto vc quer sacar: R$'))

while True:
   q50 = v/(c*50)
   if q50 >= 1:
       cont50 = cont50 + 1
       c = c + 1
   else:
        break

if cont50 == 0:
    print('', end='')
else:
    print(f'{cont50} notas de R$50')
c = 1

while True:
   q20 = (v - cont50*50)/(c*20)
   if q20 >= 1:
       cont20 = cont20 + 1
       c = c + 1
   else:
        break

if cont20 == 0:
    print('', end='')
else:
    print(f'{cont20} notas de R$20')
c = 1

while True:
   q10 = (v - cont50*50 - cont20*20)/(c*10)
   if q10 >= 1:
       cont10 = cont10 + 1
       c = c + 1
   else:
        break

if cont10 == 0:
    print('', end='')
else:
    print(f'{cont10} notas de R$10')
c = 1

q1 = (v - cont50*50 - cont20*20 - cont10*10)/(c*1)
if q1 == 0:
    print('', end='')
else:
    print(f'{q1:.0f} notas de R$1')