#https://inf-ege.sdamgia.ru/problem?id=58490
def f(x, y):
    if x == y:
        return 1
    if x == 11 or x == 15:
        return 0
    if x > y:
        return 0
    return f(x*2, y) + f(x+1, y) + f(x+3, y)


print(f(2, 8)*f(8, 20))
