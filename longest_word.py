# In this challenge you need to find the longest word in a sentence. 
# If the sentence has more than one word of the same length you should pick the first one.


import sys

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","").strip().split()
		
		arr = list()
		
		for i in range(len(row)):
			for j in range(i+1, len(row)):
				if len(row[i]) < len(row[j]):
					temp = row[i]
					row[i] = row[j]
					row[j] = temp
		print row[0]					