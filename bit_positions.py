# If it is a 1 based bit position then the lowest bit is considered to be starting at position 1 instead of position 0 

import sys, math

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","").split(",")
		
		bstring = str(bin(int(row[0]))).replace("0b","").strip()
		rev = bstring[::-1]
		
		if rev[int(row[1])-1] == rev[int(row[2])-1]:
			print "true"
		else:
			print "false"
		
		