def exponent(x, n):
    r = 1
    for i in range(n):
        r *= x
    return r

print(exponent(2, 4))