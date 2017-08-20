def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]  # Swap elements. Gathers smaller elems before pivot. "Walk" pivot to middle
                break
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break  # Reached area before pivot
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break


def dutch_flag_partition2(pivot_index, A):
    pivot = A[pivot_index]
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1  # Start from last element swapped to since all before it are smaller than pivot.
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1  # Similar as above just in decreasing order


def dutch_flag_partition3(pivot_index, A):
    pivot = A[pivot_index]
    smaller = 0
    equal = 0
    larger = len(A)
    while equal < larger:
        if A[equal] < pivot:  # Swap with last smaller
            A[equal], A[smaller] = A[smaller], A[equal]
            smaller += 1
            equal += 1
        elif A[equal] == pivot:  # Leave in place move to next unclassified
            equal += 1
        else:  # Swap with first larger
            larger -= 1
            A[equal], A[larger] = A[larger], A[equal]
