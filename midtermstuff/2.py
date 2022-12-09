a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
kol = 0
for x in range(1000):
    if a * x**3 + b * x**2 + c * x + d == 0 and x != e:
        kol += 1
print(kol)


