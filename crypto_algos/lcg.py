import math

def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        print(seed)

if __name__=="__main__":
    lcg(10, 1, 10, 3)
