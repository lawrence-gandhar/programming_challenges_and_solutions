#!/usr/bin/env python

import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.replace("\n","").split(" ")
		
		sum = 0
		for x in test:
			sum += (int(x[0])*2) + int(x[1]) + (int(x[2])*2) + int(x[3])
		
		if sum%10 > 0:
			print "Fake"
		else:
			print "Real"
		
