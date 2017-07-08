import operator

def quicktotient(prime_factors, n = 0):

	'''

	Given a list of prime factors, quicktotient will
	generate the totient of their product quickly.
	
	NOTE: These factors have to be in SIMPLEST FORM.
	i.e. quicktotient([4,5,7]) does NOT output the correct answer because
	the 4 element is 2^2.
	Rather, quicktotient([2,5,7]) outputs the correct answer.
	'''

	if n == 0:
		prod = product(prime_factors)

	else:
		prod = n

	subr = prod / prime_factors[0]
	prod -= subr

	if len(prime_factors) == 1: # last item in the list:
		return prod

	return quicktotient(prime_factors[1:], prod)

def product(iterable):
    return reduce(operator.mul, iterable, 1)