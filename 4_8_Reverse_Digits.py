def reverse(x):
    res = 0
    # Reverses digits in number using mod and division only
    while x:
        res = res * 10 + x % 10
        x //= 10
    return res


