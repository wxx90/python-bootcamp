def f(x):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        return True
    else:
        return False


for y in range(2000, 2100):
    if f(y):
        print(y)
