#SOLUÇÃO ESTÁ ERRADA!
l = list()
e = str(input('Digite uma expressão: ')).strip()
x = True

for c in range(0, len(e)):
    l.append(e[c])

if l.count('(') != l.count(')') or l[0] == ')' or l[len(l)-1] == '(':
    print('A expressão não é válida 12!')
    x = False

elif l[0].isalnum() == False and l[0] != '(' or l[len(l)-1].isalnum() == False and l[len(l)-1] != ')':
    print('A expressão não é válida 13!')
    x = False
else:
    for c in range(0, len(l)):
        if l[c] == '(' and l[c+1].isalnum() == False and l[c+1] != '(':
            print('A expressão não é válida 14')
            x = False
            break
        elif l[c] == ')' and l[c-1].isalnum() == False and l[c-1] != ')':
            print('A expressão não é válida 15')
            x = False
            break

if x:
    print('A expressão é válida!')

    #(a+b)*c)((a-b)*d