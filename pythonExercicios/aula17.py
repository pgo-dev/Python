num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
#num[4] = 7
num.append(7)
print(num)

num.sort()
print(num)
num.sort(reverse=True)
print(num)

print(f'essa lista tem {len(num)} elementos')

'''num.insert(2, 0)
print(num)'''''

'''num.pop()
print(num)'''

'''num.pop(2)
print(num)'''

num.insert(2, 3)
print(num)
if 5 in num:
    num.remove(5)
else:
    print('Não existe 4 na lista!')
print(num)

l = [2, 35, 6]
l.insert(-1, 1)
print(l)

