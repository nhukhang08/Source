def is_prime(n):
	if n in [2,3]: return True
	elif n % 2 == 0 or n % 3 == 0: return False
	for i in range(5, int(n**0.5)+1, 6):
		if n % i == 0 or n % (i+2) == 0: False
	return True