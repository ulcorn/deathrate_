f = open('input.txt')
s = f.readlines()
summa = 0
slov = {}
for i in s:
    i = i.split()
    summa += int(i[-1])
    x = i[:-1]
    h = ''
    for o in x:
        h += (o + ' ')
    slov[h] = int(i[-1])
    # print(*i[:-1], i[-1])
a = summa/450
b = 450/summa
elsesum = 0
if a >= 1:
    for x in slov:
        print(x, round(slov[x]/a))
else:
    for x in slov:
        elsesum += round(slov[x]*b)
    if elsesum < 450:
        for o in slov:
            slov[o] += (450 - elsesum)/b
            break
    for i in slov:
        print(i, round(slov[i]*b))