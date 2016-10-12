import sys

test_cases = open(sys.argv[1], 'r')
words = {"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}

for test in test_cases:
    a = test.split(";")
    j = ''
    for f in a:
        f = f.replace("\n","")
        j = j + str(words[f])
    print j
    
test_cases.close()