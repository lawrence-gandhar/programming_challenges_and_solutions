#!/usr/bin/env python

import sys

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		j = test.replace("\n","").split(" ")
		q = [float(x) for x in j]
		gg = sorted(q)
		
		for g in gg:
			print "%.3f" %g,
		print
		
		
