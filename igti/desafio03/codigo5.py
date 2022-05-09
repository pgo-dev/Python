class classe1:
    def func(self, string):
        dic = {'I':1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        valor = 0
        for i in range(len(string)):
            if i > 0 and dic[string[i]] > dic[string[i - 1]]:
                valor += dic[string[i]] - 2 * dic[string[i -1]]
            else:
                valor += dic[string[i]]
        return valor

x = classe1.func(1, 'XV')

print(x)
