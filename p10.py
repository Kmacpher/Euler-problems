import math
def is_prime(n):
	if (n%2==0 and n>2) or n==1:
		return False
	return all(n%i for i in range(3, int(math.sqrt(n)) + 1, 2))

print sum(x for x in xrange(2000000) if is_prime(x))

#apparently I forgot what a factor means! This is silly. This gives the 
#highest prime number less than that number. I need to factor it out somehow
