import math

def is_prime(n):
        if n%2==0 and n>2:
                return False
        return all(n%i for i in range(3, int(math.sqrt(n)) + 1, 2))

def primelist(target):
	prime = [2]
	n = 3	
	while True:
		if is_prime(n):
			prime.append(n)
		if len(prime) == target:
			return prime[-1]
		n=n+2

print primelist(10001)
