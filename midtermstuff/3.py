from itertools import combinations as cm
a = int(input())
seg = list(map(int, input(). split()))
kol = 0
for i in cm(seg, 3):
    i = sorted(i)
    if i[2] < i[0] + i[1]:
        kol += 1
print(kol)


