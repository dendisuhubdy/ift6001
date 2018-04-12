def merge_step(x, y, result):

    if x[0] == 1:
        if y[0] == 0 and len(result) == 0:
            result.append(1)

    if x[0] == 0 and y[0] == 0:
        if len(result) > 0:
            result[len(result) -1] = result[len(result) -1] + 1


def divide_and_conquer(array, result):
    # [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1]

    if len(array) == 1:
        return merge_step([array], [array], result)

    mid = len(array) // 2
    x = array[:mid]
    y = array[mid:]

    divide_and_conquer(x, result)
    divide_and_conquer(y, result)
    merge_step(x, y, result)

    if len(result) == 0:
        return 0
    return max(result)

def solution(N):
    # write your code in Python 2.7
    array = [int(x) for x in "{0:b}".format(N)]
    return divide_and_conquer(array, [])


if __name__=="__main__":
    print(solution(1041))
    print(solution(15))
