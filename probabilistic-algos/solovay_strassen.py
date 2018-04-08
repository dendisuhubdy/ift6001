import math
import random
import numpy as np

from sys import exit
from prime import prime

def i4_is_prime ( n ) :
    from math import floor
    from math import sqrt

    if ( n <= 0 ):
        value = False
        return value

    if ( n == 1 ):
        value = False
        return value

    if ( n <= 3 ):
        value = True
        return value

    nhi = int ( sqrt ( float ( n ) ) )

    for i in range ( 2, nhi + 1 ):
        if ( ( n % i ) == 0 ):
            value = False
            return value

    value = True

    return value

def legendre_symbol ( q, p ):

    l = 0
    #
    #  P must be greater than 1.
    #
    if ( p <= 1 ):
        print ( '' )
        print ( 'LEGENDRE_SYMBOL - Fatal error!' )
        print ( '  P must be greater than 1.' )
        l = -2
        exit ( 'LEGENDRE_SYMBOL - Fatal error!' )
    #
    #  P must be prime.
    #
    if ( not ( i4_is_prime ( p ) ) ):
        print ( '' )
        print ( 'LEGENDRE_SYMBOL - Fatal error!' )
        print ( '  P is not prime.' )
        l = -3
        exit ( 'LEGENDRE_SYMBOL - Fatal error!' )
    #
    #  ( k*P / P ) = 0.
    #
    if ( ( q % p ) == 0 ):
        l = 0
        return l
    #
    #  For the special case P = 2, (Q/P) = 1 for all odd numbers.
    #
    if ( p == 2 ):
        l = 1
        return l

    #
    #  Make a copy of Q, and force it to be nonnegative.
    #
    qq = q

    while ( qq < 0 ):
        qq = qq + p

    nstack = 0
    pstack = np.zeros ( 100 )
    qstack = np.zeros ( 100 )
    pp = p
    l = 1

    while ( True ):

        qq = ( qq % pp )
        #
        #  Decompose QQ into factors of prime powers.
        #
        nfactor, factor, power, nleft = i4_factor ( qq )

        if ( nleft != 1 ):
            print ( '' )
            print ( 'LEGENDRE_SYMBOL - Fatal error!' )
            print ( '  Not enough factorization space.' )
            l = -5
            exit ( 'LEGENDRE_SYMBOL - Fatal error!' )
        #
        #  Each factor which is an odd power is added to the stack.
        #
        nmore = 0

        for i in range ( 0, nfactor ):

            if ( ( power[i] % 2 ) == 1 ):

            nmore = nmore + 1
            pstack[nstack] = pp
            qstack[nstack] = factor[i]
            nstack = nstack + 1

        hop = False

        if ( nmore != 0 ):
            nstack = nstack - 1
            qq = qstack[nstack]
        #
        #  Check for a QQ of 1 or 2.
        #
        if ( qq == 1 ):

            l = + 1 * l

        elif ( qq == 2 and ( ( pp % 8 ) == 1 or ( pp % 8 ) == 7 ) ):

            l = + 1 * l

        elif ( qq == 2 and ( ( pp % 8 ) == 3 or ( pp % 8 ) == 5 ) ):

            l = - 1 * l

        else:

            if ( ( pp % 4 ) == 3 and ( qq % 4 ) == 3 ):
                l = - 1 * l

        rr = pp
        pp = qq
        qq = rr

        hop = True
        #
        #  If the stack is empty, we're done.
        #
        if ( not hop ):
            if ( nstack == 0 ):
            break
        #
        #  Otherwise, get the last P and Q from the stack, and process them.
        #
        nstack = nstack - 1
        pp = pstack[nstack]
        qq = qstack[nstack]

    return l


def i4_factor ( n ):
    nfactor = 0
    factor = []
    power = []
    nleft = n

    if ( n == 0 ):
        return nfactor, factor, power, nleft

    if ( abs ( n ) == 1 ):
        nfactor = 1
        factor.append ( 1 )
        power.append ( 1 )
        return nfactor, factor, power, nleft
    #
    #  Find out how many primes we stored.
    #
    maxprime = prime ( -1 )
    #
    #  Try dividing the remainder by each prime.
    #
    for i in range ( 1, maxprime + 1 ):

        p = prime ( i )

        if ( ( ( abs ( nleft ) ) % p ) == 0 ):

            nfactor = nfactor + 1
            factor.append ( p )
            power.append ( 0 )

        while ( True ):

            power[nfactor-1] = power[nfactor-1] + 1
            nleft =  ( nleft // p )

        if ( ( ( abs ( nleft ) ) % p ) != 0 ):
            break

        if ( abs ( nleft ) == 1 ):
            break

    return nfactor, factor, power, nleft


def jacobi_symbol ( q, p ):
    from legendre_symbol import legendre_symbol
    #
    #  P must be greater than 1.
    #
    if ( p <= 1 ):
        print ( '' )
        print ( 'JACOBI_SYMBOL - Fatal error!' )
        print ( '  P must be greater than 1.' )
        j = -2
        return l
    #
    #  Decompose P into factors of prime powers.
    #
    nfactor, factor, power, nleft = i4_factor ( p )

    if ( nleft != 1 ):
        print ( '' )
        print ( 'JACOBI_SYMBOL - Fatal error!' )
        print ( '  Not enough factorization space.' )
        j = -2
        return j
    #
    #  Force Q to be nonnegative.
    #
    qq = q

    while ( qq < 0 ):
        qq = qq + p
    #
    #  For each prime factor, compute the Legendre symbol, and
    #  multiply the Jacobi symbol by the appropriate factor.
    #
    j = 1
    for i in range ( 0, nfactor ):
        pp = factor[i]
        l = legendre_symbol ( qq, pp )
        if ( l < -1 ):
            print ( '' )
            print ( 'JACOBI_SYMBOL - Fatal error!' )
            print ( '  Error during Legendre symbol calculation.' )
        j = -3

    j = j * l ** power[i]

    return j


def solovay_strassen(n, k):
    i = 0
    while i < k:
        a = random.randint(2, n-1)
        x = jacobi_symbol(a, n)
        if x = 0 or a ** (n -1)/2 not congru with x mod n:
            return "composite"
        return "probably prime"


