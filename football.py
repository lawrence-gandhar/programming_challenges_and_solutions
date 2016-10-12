#!/usr/bin/env python
import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	main = test.replace("\n","")
	data = main.split(" | ")
	g = dict()
	i = 0
	for x in data:
		g[i] = x
		i += 1

	s = vv = list()
	for x in g:
		ds = g[x].split(" ")		
		for dss in ds:
			if dss not in vv:
				vv.append(dss)
	vv = map(int, vv)	
	vv.sort()

	for x1 in vv:
		gg = ''
		for x in g:
			ds = g[x].split(" ")	
			if str(x1) in ds:
				xss = x + 1
				gg += str(xss)+","
		
		print str(x1)+":"+gg.rstrip(",")+";",
	print	
