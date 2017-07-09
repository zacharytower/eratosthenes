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
