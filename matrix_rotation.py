# Simple Logic on the turn of 90degrees clockwise 
# the last row will become the first column of the matrix of NxN
# For anticlockwise rotation it will make the last row to last column in the matrix

# In the file we have to count the number of elements in each row
# to get the (N) of the array and generate it
# Since its a NxN matrix, the sqrt(no.of elements) = m 

import sys, math

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","")
		
		if row!= "":
			row = row.split(" ")
			
			M = int(math.sqrt(len(row)))
			
			temp_list = list()
			js_list = list()
			
			j = 0
			for i in range(M):
				temp_list.append(list())
				
				x = 0
				while x < M:
					temp_list[i].append(list())
					temp_list[i][x] = row[j]
					x += 1
					j += 1
		
			N = M
			
			for j in range(N):
				for i in range(M-1, -1, -1):
					js_list.append(temp_list[i][j].strip())
			
			print ' '.join(js_list)
		
		