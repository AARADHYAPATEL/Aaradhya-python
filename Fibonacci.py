n = 10
a, b = 0, 1
print(a)
print(b)

for _ in range(n - 2):
    c = a+b
    print(c)
    a, b = b, c