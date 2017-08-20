def multiplication(num1, num2):
    """Gradeschool multiplication algorithm using arrays representing integers"""
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    result = [0 for x in range(len(num1) + len(num2))]
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10  # Add the carry if result[i + j + 1} > 9
            result[i + j + 1] %= 10  # Strip last digit
    # Why you do dis? Would be better understood as a multiline loop
    result = result[next((i for i, x in enumerate(result) if x != 0), len(result)):] or [0]
    return [sign * result[0]] + result[1:]
