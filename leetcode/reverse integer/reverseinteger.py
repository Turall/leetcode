def rev_int(x):
    temp = 0
    imax = 2147483647
    imin = -2147483648
    tag = False
    if x < imin or imax < x:
        return 0
    if x < 0:
        tag = True
        x *= -1
    while x > 0:
        tempx = x % 10
        temp = (temp * 10) + tempx
        x = x // 10
    if tag:
        temp *= -1
    if temp < imin or temp > imax:
        return 0
    return temp


print(rev_int(123))

