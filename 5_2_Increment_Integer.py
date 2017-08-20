def plus_one(A):
    """Grade school addition algorithm. Compare to bit shift addition in 4_5_Compute_x_time_y.py"""
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 0
        A.insert(0, 1)
    return A
