def fibo(limit):
	seq = [1, 2]
	while True:
		if seq[-1]+seq[-2] > limit:
			return seq
		else:
			seq.append(seq[-1] + seq[-2])

def sum_even(alist):
	return sum(x for x in alist if x%2 == 0)

print sum_even(fibo(4000000))

