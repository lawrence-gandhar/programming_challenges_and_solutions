import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    a = test.split(":")
    data_list = a[0]
    swap_ranges = a[1] 
    swap_range_list = swap_ranges.split(",")
    
    temp_list = data_list.split()

    for t in range(len(swap_range_list)):
    	
    	ta = swap_range_list[t].split("-")
    	
    	temp = temp_list[int(ta[0])]
    	temp_list[int(ta[0])] = temp_list[int(ta[1])]
    	temp_list[int(ta[1])] = temp
    	temp_list = temp_list

    print ' '.join(temp_list)
test_cases.close()


 
