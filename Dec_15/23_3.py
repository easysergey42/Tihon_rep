#https://inf-ege.sdamgia.ru/problem?id=16898
def f(x,y):
    if x == y:
        return 1
    if x == 5 or x == 10:
        return 0
    if x > y:
        return 0
    return f(x+1,y) + f(x*2,y) + f(x+3,y)


print(f(2,14))