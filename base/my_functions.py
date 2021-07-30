def my_max(m, n):
    if m > n:
        return m
    else:
        return n


a, b = 4, 6
print((my_max(a, b)))

t = lambda m, n: m if m > n else n

a, b = 1, 3
print(t(a, b))
