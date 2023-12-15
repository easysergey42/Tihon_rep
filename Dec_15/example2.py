

def fn(n):
    if n < 4:
        return n - 1
    if n >= 4:
        if n % 3 == 0:
            return n + 2 * fn(n-1)
        else:
            return fn(n-2) + fn(n-3)
        
print(fn(1000))