#!/usr/bin/env python

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	main = test.replace("\n","")
	data = main.split(",")
	
	i = 0
	temp = -1
	while i < len(data[0]):
		if data[0][i] == data[1]:
			temp = i	
		i += 1

	print temp

test_cases.close()
