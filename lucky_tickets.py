import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = int(test.replace("\n",""))
    
    start_boundary = 10**(test-1)
    end_boundary = 10**(test)

    count = 1
    while start_boundary < end_boundary:
        y = str(start_boundary)
        half1 = y[:test/2]
        half2 = y[test/2:]

        temp1 = int(half1)
        temp2 = int(half2)

        sum1 = 0
        while temp1 > 0:
            rem1 = temp1 % 10
            sum1 = sum1 + rem1
            temp1 = temp1 / 10

        sum2 = 0
        while temp2 > 0:
            rem2 = temp2 % 10
            sum2 = sum2 + rem2  
            temp2 = temp2 / 10  

        if sum1 == sum2:
            count = count + 1   
            #print i, count 

        start_boundary = start_boundary + 1    
    print(count) 


test_cases.close()