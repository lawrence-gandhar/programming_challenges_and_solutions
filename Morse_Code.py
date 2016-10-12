#!/usr/bin/env python

import sys

arr = dict({'a' : '.-' ,'b' : '-...' ,'c' : '-.-.' ,'d' :'-..', 'e' : '.', 'f' : '..-.' , 'g' : '--.', 'h' : '....' , 'i' : '..' , 'j' : '.---' , 'k' : '-.-' , 'l' : '.-..' , 'm' : '--' , 'n' : '-.' , 'o' : '---' , 'p' : '.--.' , 'q' : '--.-' , 'r' : '.-.' , 's' : '...' , 't' : '-' , 'u' : '..-' , 'v' : '...-' , 'w' : '.--' , 'x' : '-..-' , 'y' : '-.--' , 'z' : '--..' , '0' : '-----' , '1' : '.----' , '2' : '..---' , '3' : '...--' , '4' : '....-' , '5' : '.....' , '6' : '-....' , '7' : '--...' , '8' : '---..' , '9' : '----.' })

arr2 = dict((value, key) for key, value in arr.iteritems())


with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.replace("\n","").split("  ")
		
		ff = ''
		
		for s in test:
			g = s.split(" ");
			for x in g:
				ff += arr2[x].upper()
			ff += " "	
		print ff		
					
			
