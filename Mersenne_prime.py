import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test.replace("\n","")
		strn = ''
		for execp in [2,3]:
			if (2**execp)-1 > int(test):
				break
			else:
				strn = strn + str((2**execp)-1) + ", "

		i = 1
		while i >= 1:

			if ((2**((6 * i) - 1)) - 1) > int(test):
				break
			else:
				strn = strn + str((2**((6 * i) - 1))-1) + ", "
				
			if ((2**((6 * i) + 1)) - 1) > int(test):
				break
			else:
				strn = strn + str((2**((6 * i) + 1))-1) + ", " 
			
			i = i + 1

		print(strn.rstrip(", "))
	
