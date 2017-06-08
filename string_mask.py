
import sys, math

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","").split(" ")
		
		data = row[0]
		mask = row[1]
		data_p = ''
		for i in range(len(data)):
			if mask[i] == '1':
				data_p += data[i].upper()
			else:
				data_p += data[i]
				
		print data_p	