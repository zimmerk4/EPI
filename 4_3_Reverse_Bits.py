def reverse_bits(x):
    """Create a lookup table of precomputed parities and use them to calculate
    the parity of the 8-bit word."""
    MASK_SIZE = 2
    BIT_MASK = 0x3
    REV_LOOKUP = [0, 2, 1, 3]  # binary inverses of 00, 01, 10, 11
    # Returns value at index. Isolates 16 bit chunks by shifting/anding
    return (REV_LOOKUP[x & BIT_MASK] << (3 * MASK_SIZE) |
            REV_LOOKUP[(x >> MASK_SIZE) & BIT_MASK] << (2 * MASK_SIZE) |
            REV_LOOKUP[(x >> (2 * MASK_SIZE)) & BIT_MASK] << MASK_SIZE |
            REV_LOOKUP[(x >> (3 * MASK_SIZE)) & BIT_MASK])
