#https://inf-ege.sdamgia.ru/problem?id=3792
def fn(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    return fn(a+1, b) + fn(a*4,b)

print(fn(1,29))