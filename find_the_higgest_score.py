# The first argument is a path to a file. 
# Each line includes a test case with a table. Table rows are separated by pipes '|'. 
# All table rows contain scores for each category, so all lines are of an equal length
# You need to print the highest score for each category.

import sys

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","").strip().split("|")
		
		arr = list()
		for row in row:
			row = row.strip().split(" ")		
			arr.append(row)
			
		no_of_cols = len(arr[0])
		no_of_rows = len(arr)
		
		
		main_rank_list = list()
		for col in range(no_of_cols):
			
			gs_list = list()
			for row in range(no_of_rows):
				gs_list.append(int(arr[row][col]))
		
			gs_list.sort()	

			main_rank_list.append(str(gs_list[-1]))	

		print ' '.join(main_rank_list)
		
		