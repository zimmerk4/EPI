def swap_bits(x, i, j):
    """Swap bits by seeing if they differ and flipping their values if so"""
    # Extract i-th and j-th bit to see if the differ.
    if (x >> i) & 1 != (x >> j) & 1:
        # Create bit_mask with 1 at location of i and j then XOR to flip vals
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

