# Determine max sum at the range.

import sys

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","").strip().split(";")
		days = int(row[0])
		data = row[1].split(" ")
		
		days_list = list()	
			
		for i in range(len(data)):
			counter = 0
			sum = 0
			
			while counter < days:
				if (i + days - 1) < len(data):					
					sum += int(data[i + counter])
				else:
					break	
				counter += 1
				
			if sum < 0 :
				sum = 0

			days_list.append(sum) 	
		
		days_list.sort()
		print days_list[-1]