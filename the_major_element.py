# The major element in a sequence with the length of L is the element which appears in a sequence more than L/2 times. 
# The challenge is to find that element in a sequence.


import sys

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","").strip().split(",")
		sequence_len = len(row)
		
		distinct_sqn = list()
		count_man = dict()
		
		row.sort()
		for x in row:
			if x not in distinct_sqn:
				distinct_sqn.append(x)
				
			if x not in count_man.keys():
				count_man[x] = 1
			else:
				count_man[x] += 1 

		grt_count = dict()
		
		for x in distinct_sqn:
			if count_man[x] > sequence_len/2:
				grt_count[x] = count_man[x]
		
		if len(grt_count) == 0:
			print "None"
		else:
			print ''.join(grt_count.keys())	