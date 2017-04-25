# Calculate the distance between two given points


import sys, re, math

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","").strip()
		
		cordinates = re.findall('\(.*?\)',row)
		
		cordinates1 = cordinates[0].replace("(","").replace(")","").strip().split(", ")
		cordinates2 = cordinates[1].replace("(","").replace(")","").strip().split(", ")
		
		print int(math.sqrt(((int(cordinates2[0])-int(cordinates1[0]))**2) + ((int(cordinates2[1])-int(cordinates1[1]))**2)))
		
		
		
		