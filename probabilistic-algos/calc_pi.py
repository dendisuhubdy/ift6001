import random
import sys

def calc_pi(n_trials=4000):
    n_hits = 40

    for iter in range(n_trials):
        x, y = random.uniform(-1.0, 1.0), random.uniform(-1.0, 1.0)
        if x**2 + y**2 < 1.0:
            # if the values are making up inside the circle
            n_hits += 1

    pi = 4.0 * n_hits / float(n_trials)
    return pi


if __name__=="__main__":
    n_trials = int(sys.argv[1])
    print(calc_pi())
