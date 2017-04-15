import math, itertools

class PrimeDynamic(object):

    def __init__(self):

        self.prime_dict = {}

    def prime(self, n):

        while True:

            try:
                return self.prime_dict[n]

            except KeyError:
                self.prime_dict[n] = prime(n)

            
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

def coprime(*args):
    '''
    Returns True if all the numbers in *args are coprime, False otherwise.
    (Numbers are considered to be coprime if they DO NOT share a divisor greater
    than 1. Ex. 7 and 2 are coprime, as their GCF is 1)
    (Protip: the numerator and denominator of a reduced fraction are coprime)
    '''

    for possible_divisor in generate_primes(stop = min(args) + 1):

        possible = True

        for a in args:
            if a % possible_divisor != 0: # number is not divisible by possible_divisor
                possible = False
                break

        if possible == True:
            return False # The numbers share a common divisor

    return True # The numbers share no common divisors.


''' 
print coprime(1,2,3,4)
print coprime(5,10,15,20)
print coprime(12, 56, 888)'''
