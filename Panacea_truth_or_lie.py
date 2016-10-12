import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		x = test.replace("\n","").split(" | ")
		
		hexa = x[0].split(" ")
		binary = x[1].split(" ")

		h_sum = b_sum = 0
		for h in hexa:
			h_sum = h_sum + int(str(h),16)
		
		for b in binary:
			b_sum = b_sum + int(str(b),2)

		if b_sum >= h_sum :
			print("True")
		else:
			print("False")
