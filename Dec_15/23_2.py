#https://inf-ege.sdamgia.ru/problem?id=14708
def f(x,y):
    if x == y:
        return 1
    if x > y:
        return 0
    return f(x+1,y) + f(x*2,y)


print(f(1,10) * f(10,21) * f(21,30))