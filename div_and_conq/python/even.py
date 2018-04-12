def even_one(m):
    """
    Given only additions and subtractions
    computations determine of a number m
    is even or odd
    """

    if m == 0:
        return True

    if m == 1:
        return False

    return even_one(m - 1 - 1)


def even_two(m):
    """
    Given only additions and subtractions
    computations determine of a number m
    is even or odd
    """

    if m == 0:
        return True

    if m == 1:
        return False

    i = 1
    j = m

    while i < j:
        i = i + 1
        j = j - 1
        print(i, j)

    return even_two(m)


if __name__=="__main__":
    m = 100

    print(even_one(m))

    print(even_two(m))
