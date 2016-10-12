#!/usr/bin/env python
import sys

def check_occurance(word,checklist):
	count = 0
	temp = word 
	for x in checklist:
	       	if temp.find(x)!=-1:
			temp = temp.replace(x,'',1)
			count = count + 1	
	
	if count == len(checklist):
	       	return word
	else:
	       	return False

g = list()
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	main = test.replace("\n","")
	data = main.split(" | ")
	if len(data) > 1:
		g.append(data)

ds = list()			 	
for line in g:
	if len(line)> 0:
		js = list()
		for word in line[0].split(" "):
			if check_occurance(word, line[1])!=False:
				js.append(word) 
			else:
				js.append('false')	
	if len(js)>0:
		ds.append(js)

dg = list()
for d in ds:
	dk = " ".join(d)
	vf = dk.replace("false",'')
	vf  = vf.split(" ")
	es = list()
	for e in vf:
		if e!='':
			es.append(e)	
 	dg.append(' '.join(es))

for e in dg:
	if e=="":
		print "False"
	else:
		print e


test_cases.close()
