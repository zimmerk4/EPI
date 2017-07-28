def parity_1(x):
    """Optimized brute force to calculate parity of x"""
    res = 0
    while x:
        res ^= 1  # Equivalent to mod 2. Only care if res is odd for parity
        x &= x-1  # Drops the lowest set bit of x
    return res


def parity_2(x):
    """Create a lookup table of precomputed parities and use them to calculate
    the parity of the 8-bit word."""
    MASK_SIZE = 2
    BIT_MASK = 0xF
    PRECOMPUTED_PARITY = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0,
                          0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1,
                          0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0,
                          0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
                          0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0,
                          0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1,
                          0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0,
                          0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1,
                          0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1,
                          1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1,
                          0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0,
                          0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0,
                          0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1,
                          1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1,
                          0, 1, 1, 0]
    # Fill PRECOMPUTED_PARITY
    # with open('parity.txt', 'w+') as file:
    #     for x in range(0x100):
    #         file.write(str(parity_3(x)) + ", ")
    print(len(PRECOMPUTED_PARITY))
    # Returns XOR of vals at indices. Isolates 16 bit chunks by shifting/anding
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])


def parity_3(x):
    """Calculates parity of 64 bit word using fact that XOR of group of bits is
    parity"""
    # Splits length of word in powers of 2 and XORs
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1  # Last bit is answer so extract it by anding with 1

