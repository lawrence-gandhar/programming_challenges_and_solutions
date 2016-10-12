import sys

def bin(t):
	temp = t
	g = list()
	if temp == 0:
		return 0
	else:	
		while temp > 0:
			g.append(str(temp%2))
			temp = temp/2
		g.reverse()	
		return ''.join(g)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	t1 = int(test.replace("\n",""))
	print bin(t1)	
test_cases.close()	