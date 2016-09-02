import math, itertools

def eratosthenes(n):

    ''' Sieve of Eratosthenes.
        Generates all prime numbers from 2 to n.'''


    numbers = {}

    for x in range(2,n+1):
        numbers[x] = False

    
    for x in range(2,n + 1):

        if numbers[x] == False : # number is prime:
            yield x

            if x ** 2 > n:

                for y in range(x+1,n+1):
                    
                    if numbers[y] == False: # number is unmarked
                        yield y



                break

            for d in range(x ** 2,n + 1,x):
                numbers[d] = True # mark all multiples

def prime(n, oneIsPrime = False):

    if n == 1: return oneIsPrime
    for x in range(2,int(math.sqrt(n)) + 1):
        if n % x == 0:
            return False

    return True

def generate_primes(start = 2,stop = None):

    ''' generator that generates prime numbers.
    Starts at 'start' (default 2) and stops at 'stop' (default None)
    If stop is none, it will generate primes infinitely.'''


    step = 1 if start % 2 == 0 else 2

    if stop == None:
        gen = itertools.count(start, step)
    elif start > stop:
        gen = range(start,stop,-step)
    else:
        gen = range(start,stop,step)

    for x in gen:
        if x == stop: break

        if prime(x): yield x

        step = 2

def spd(n):
    ''' returns the smallest prime divisor of a number.'''
    for p in generate_primes(2):
        if n % p == 0:
            return p

    