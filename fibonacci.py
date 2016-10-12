import sys

test_cases = open(sys.argv[1], 'r')

for test in test_cases:
	test = int(test.replace("\n",""))
	f = 0
	sums = 0
	while f <= test:
		if f == 0:
			sums = 0

		if f == 1:
			term1 = f
			term2 = sums	
			sums = term1 + term2

		if f >= 2:	 
			term1 = term2
			term2 = sums

			sums = term1 + term2	

		f = f + 1
		#print sums,
   	print sums	
    
test_cases.close()