from datetime import datetime

now = datetime.now()
print(now.year, now.month, now.day)


def f(a, b, c):
    return a+b+c


def max(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a1, b1, c1):
    m1 = max(a1, b1)
    m2 = max(b1, c1)
    return max(m1, m2)


print(max3(10, 8, 6))


def calc_age(year, month, day):
    return 10


print(calc_age(1990, 10, 1))
