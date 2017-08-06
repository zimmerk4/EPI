# Multiply x and y using only assignment, bitwise ops, and equality checks.
def multiply(x, y):
    run_sum = 0
    while x:
        if x & 1:  # Adds y*2^k for each set bit in x where k is location of the set bit
            run_sum = add(run_sum, y)
        x >>= 1
        y <<= 1
    return run_sum


def add(a, b):
    while b != 0:  # Terminates when no carries are left
        carry = (a & b)  # Finds all carries where both a and b have a 1 bit
        a = a ^ b  # Sets all bits in a+b that don't cause carries
        b = carry << 1  # Shifts the carry bits to be added in next iteration
    return a

