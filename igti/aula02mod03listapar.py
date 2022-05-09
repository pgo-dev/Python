l = int(input('Tamanho da lista: '))
list = []
list3 = []

for c in range(0, l):
    list.append(c * 2)
print(list)

list2 = [l for l in range(1, (l)*2) if l%2 !=0]
print(list2)

i = j =0
for c in range(len(list)+len(list2)):
    if c % 2 == 0:
        list3.append(list[i])
        i+=1
    else:
        list3.append(list2[j])
        j+=1
print(list3)
