import sys
from sets import Set

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.replace("\n","")
    t = test.split(";")
    l = list()
    for f in t:
        x = f.split(",")
        l.append(x)    
    set1 = set(l[0])
    set2 = set(l[1])

    d = sorted(set1 & set2)
    print ','.join(d)

test_cases.close()