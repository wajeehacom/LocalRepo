def move_zeros(lst):
    result = []
    zeros = 0

    for num in lst:
        if num == 0:
            zeros += 1
        else:
            result.append(num)

    result.extend([0] * zeros)
    return result


print(move_zeros([1, 0, 2, 0, 4, 0, 5]))



    