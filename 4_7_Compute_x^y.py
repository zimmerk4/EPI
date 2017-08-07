def power_x_y(x, y):
    res = 1.0
    power = y
    if y < 0:
        power = -y
        x = 1.0/x
    # Recursively squares x for each power of 2 in y. Odd powers are tracked by multiplying res by x
    while power:
        if power & 1:
            res *= x
        x = x * x
        power >>= 1
    return res



