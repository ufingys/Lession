def gen(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
        yield res


generator = gen(10)
for el in generator:
    print(el, end=' ')