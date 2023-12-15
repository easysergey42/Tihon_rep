def f(n):
    if n == 1:
        return 1
    if n > 1:
        if n % 2 == 0:
            return f(n // 2) + n
        else:
            return f(n+1)
        
for n in range(1000):
    if f(n) == 105:
        print(n)
        break