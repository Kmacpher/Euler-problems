import math

def is_prime(n):
        if n%2==0 and n>2:
                return False
        return all(n%i for i in range(3, int(math.sqrt(n)) + 1, 2))

def factors(n):
	return set(reduce(list.__add__,([i,n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def topprime(factorset):
	return max(x for x in factorset if is_prime(x))
		

print topprime(factors(600851475143))
