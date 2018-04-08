"""
Implementation of RSA cryptography 
using samples of large numbers
"""

import math
import random

from millerrabin import miller_rabin


def generate_keys(p, q):
    """
    p and q should be both prime
    """
    z = p * q
    phi = (p-1)*(q-1)

    print("Phi is: " + str(phi))

    """
    It is better to obtain n
    as a prime number
    """

    n = None

    for i in range(1, z-1):
        num = random.randint(6, z-1)
        if miller_rabin(num):
            n = num
            break

    print("n is ", n)

    """
    calculate unique s such that ns(mod phi) = 1
    if it does not exist or that gcd(n, z) \neq 1
    then choose another n such that pgcd(n, z) \neq 1
    """

    print("Generating secret.............")

    i = 1
    for i in range(1, z-1):
        if ((n*i) % phi == 1):
            s = i
            break

    pub_key = [z, n]
    print("Public key is: ", pub_key)
    priv_key = s
    print("Private key is: ",  priv_key)

    return pub_key, priv_key

def fast_exp(a, n):
    a = int(a)
    n = int(n)
    if n == 1:
        return a
    if n & 1:
        return fast_exp(a, n/2) ** 2
    
    return fast_exp(a, n-1)

def encrypt(message, pub_key):
    """
    message here is a large integer
    """
    c = fast_exp(int(message), int(pub_key[1])) % int(pub_key[0])
    
    """
    c is the encrypted message
    """
    return c

def decrypt(encrypted_message, private_key, pub_key):
    c = encrypted_message

    m = fast_exp(int(c), int(private_key)) % int(pub_key[0])

    return m


def main():
    pub_key, priv_key = generate_keys(19, 23)

    message = 123
    print("Message is ", str(message))

    print("Encrypting message...........")

    enc_msg = encrypt(message, pub_key)
    
    print(enc_msg)

    print("Decrypting message...........")
    
    dec_msg = decrypt(enc_msg, priv_key, pub_key)

    print("Secret message is ", dec_msg)

if __name__=="__main__":
    main()
