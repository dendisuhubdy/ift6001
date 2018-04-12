def binsearch(list, val):
    list_size = len(list) - 1

    idx0 = 0
    idxn = list_size

    # FInd the middle most size

    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2

        if list[midval] == val:
            return midval

        # Compare the value the middle most value

        if val > list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval + 1

    if idx0 > idxn:
        return None


if __name__=="__main__":
    list = [2, 7, 19, 34, 53, 72]

    print(binsearch(list, 72))
    print(binsearch(list, 11))
