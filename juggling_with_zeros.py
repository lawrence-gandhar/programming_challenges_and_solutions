import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	t1 = test.replace("\n","").split()
	s = ''
	i = 0
	while i < len(t1):
		if t1[i] == "0":
			s = s + '0'*len(t1[i+1])

		if t1[i] == "00":
			s = s + '1'*len(t1[i+1])	
		i = i + 2
				
	print int(s,2)	
	
test_cases.close()	