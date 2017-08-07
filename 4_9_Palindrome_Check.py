import math


def is_palindrome(x):
    if x < 0:
        return False
    num_digits = math.floor(math.log10(x)) + 1
    mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // mask != x % 10:
            return False
        x %= mask  # Peel off MSD of x
        x //= 10  # Peel off LSD of x
        mask //= 100  # x is two digits shorter so decrease mask by 10^2
    return True
