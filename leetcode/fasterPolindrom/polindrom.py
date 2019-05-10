def ispolindrom(x):

    if x < 0:
        return False

    res = 0
    y = x
    while y > 0:
        mod = y % 10
        y = y // 10
        res = res * 10 + mod

    if x == res:
        return True
    else:
        return False


if __name__ == "__main__":
    ispolindrom(121)
