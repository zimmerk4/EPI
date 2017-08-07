def divide(x, y):
    res = 0
    # power = len(bin(x))  # Makes algorithm generic and quick for any length ints
    power = 32  # Makes algorithm quick for 32 bit and smaller ints
    y_power = y << power
    # Finds highest power of 2 that when multiplied by y, is less than x and subtracts it from x. i.e. y*2^k < x
    while x >= y:
        while y_power > x:
            y_power >>= 1
            power -= 1
        res += 1 << power
        x -= y_power
    return res
