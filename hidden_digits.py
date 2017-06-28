import sys

def checkValue(character):
	ascii = ord(character)
	
	if ascii >= 97 and ascii <= 106:
		return ascii - 97
	elif ascii >= 48 and ascii <= 57:
		return ascii - 48
	else:
		return ''

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.replace("\r\n","").strip()
		
		hidden_num = ''
		for i in range(len(test)):
			hidden_num += str(checkValue(test[i]))
			
		if hidden_num == "":
			print "NONE"
		else:	
			print hidden_num	

		