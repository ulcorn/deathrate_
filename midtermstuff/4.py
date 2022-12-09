x = str(input())
a = x.find('h')
b = x.rfind('h')
y = x[a + 1: b]
y = y.replace('h', 'H')
print(x[:a + 1]+y+x[b:])

