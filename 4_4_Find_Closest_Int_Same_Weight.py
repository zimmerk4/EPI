# Weight defined as number of bits set to 1 in binary representation
def closes_int_same_bit_count(x):
    NUM_UNSIGNED_BITS = 64
    for i in range(NUM_UNSIGNED_BITS - 1):
        if ((x >> i) & 1) != ((x >> (i + 1)) & 1):
            x ^= (1 << i) | (1 << (i+1))  # Swaps bit-i and bit-(i+1)
            return x
        else:
            raise Exception