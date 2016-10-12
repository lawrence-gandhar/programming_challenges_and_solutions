import sys
import collections

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test.replace("\n","")
		d = collections.OrderedDict()
		sum = 0
		for i in range(0,len(test)-1):
			found = test.find(test[i]) 
			
			if found > -1 and found != i :
				d[test[i]] += 1 
				
			else:
				d[test[i]] = 0				
	
		for key in d.keys():
			if d[key] == 0:
				print(key)
				break
