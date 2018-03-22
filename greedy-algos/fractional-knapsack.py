import sys

def ratio(v,w):
    return v/w

def forth_element(s):
    return s[3]

def knapsack(w, v, W):
    size = len(w)
    solution = []
    values = []
    # initialization of algorithm
    # O(n)
    for i in range(size):
        values.append((i, w[i], v[i], ratio(v[i], w[i])))

    print(values)
    values = sorted(values, key=forth_element, reverse=True)
    print(values)

    total_weight = 0

    i = 0

    while total_weight <= W:
        for value in values:
            index, w, v, rat = value[0], value[1], value[2], value[3]

            print(index, w, v, rat)

            if total_weight + w <= W:
                solution.append((index, w))
            else:
                solution.append(('fraction', (W - total_weight)))
                total_weight = W

        i += 1

    return solution

if __name__=="__main__":
    w = [10, 20, 80]
    v = [100, 60, 160]

    W = int(sys.argv[1])

    S = knapsack(w, v, W)

    print(S)

