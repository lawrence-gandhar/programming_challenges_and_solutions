import sys

def binary_2_graycode(binary):
	g = list()
	x = list()
	for d in binary:
		g.append(d)
	
	for i in range(len(g)):
		if i == 0:
			x.append(g[i])
		
		if i > 0 and i <= len(g)-1:
			if g[i-1] == '1':
				if g[i] == '1': x.append('0')
				if g[i] == '0': x.append('1')
			if g[i-1] == '0':
				if g[i] == '1': x.append('1')
				if g[i] == '0': x.append('0')

					
	print int("".join(x),2)


def graycode_2_binary(binary):
	g = list()
        b = list()
        for d in binary:
                g.append(d)
        
        for i in range(len(g)):
                if i == 0:
                        b.append(g[i])
		
		if i > 0:
			if g[i] == '0' and i-1 >= 0  :
				if b[i-1] == '1': b.append('1')
				if b[i-1] == '0': b.append('0')

			if g[i] == '1':
				if b[i-1] == '1': b.append('0')
				if b[i-1] == '0': b.append('1')

	return str(int("".join(b),2))


with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.replace("\n","").split(" | ")
		stri = ''
		for i in test:
			stri +=  graycode_2_binary(i) + " | "
		print stri.rstrip(" | ");
		

