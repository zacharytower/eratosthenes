from eratosthenes import coprime
def totient(n):
	'''
	Returns the number of integers k such that, for all
	1 <= k <= n, k is relatively prime to n.
	'''
	total = 0
	for k in range(1,n + 1):
		if coprime(n,k):
			total += 1

	return total
<<<<<<< HEAD
=======

>>>>>>> cd11e1ad55d7e4f6eaedf78680e6fd949032f6d7
