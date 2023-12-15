# +1 *2

def f(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x+1,y) + f(x*2,y)

# 1 -> 4
# f(1,4) = f(2,4) + f(2,4) = f(3,4) + f(4,4) + f(3,4) + f(4,4) = f(4,4) + f(6,4) + 1