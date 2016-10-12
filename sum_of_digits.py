import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test.replace("\n",""))
    sums = 0
    while(test>0):
    	rem = test%10
    	sums = rem + sums 
    	test = test/10
    print sums

test_cases.close()
