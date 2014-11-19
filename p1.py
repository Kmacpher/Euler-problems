def multipleof3or5(num):
	li = []
	for x in xrange(num):
		if x%3==0 or x%5==0:
			print x
			li.append(x)
	return sum(li)

print multipleof3or5(1000)
