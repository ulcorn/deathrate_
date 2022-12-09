s = list(map(int, input()))
for i in range(0, len(s), 2):
    s[i] *= 2
    if s[i] >= 9:
        s[i] -= 9
summa = 0
for x in s:
    summa += x
if summa % 10 == 0:
    print('YES')
else:
    print('NO')


