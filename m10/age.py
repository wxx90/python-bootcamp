from datetime import datetime

now = datetime.now()
print(now.timestamp())
print(now.year, now.month, now.day)

print(now())

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


def T(year, month, day):
    if now.month>month:
        return now.year-year
    if now.month==month:
        if now.day>=day:
            return now.year-year
        else:
            return now.year-year-1
    else:
        return now.year-year-1


def calc_age(year, month, day):
    diff_year = now.year - year
    if now.month > month:
        return diff_year
    if now.month == month:
        if now.day >= day:
            return diff_year
        else:
            return diff_year - 1
    else:
        return diff_year - 1


print(T(2023,10,19))
