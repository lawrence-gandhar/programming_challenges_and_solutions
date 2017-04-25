import sys

class RomanNumericals():
	
	def __init__(self):
	
		self.major_symbols_dict = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}
		self.symbol_keys = self.major_symbols_dict.keys()
		self.symbol_keys.sort()
	
	
	#********************************************************************************************
	# Setting Place Value of the digits and call functions depending on them
	#********************************************************************************************
		
	def divider(self,digit = ""):
		listme = list()
		temp = digit
		counter = 0
		second_order1 = list() 
		string = ""
		
		while temp > 0:
			listme.append((temp % 10) * pow(10,counter)) 
			counter += 1
			temp = temp / 10
			
		if listme[0] > 0:
			string += self.first_order(listme[0])
		
		second_order1 = [string] + second_order1	
		
		for i in range(1,len(listme)):
			second_order1 = [self.second_order(listme[i],i)] + second_order1
		
		return ''.join(second_order1)
		
		
	#********************************************************************************************
	# Fetching the major symbol index
	#********************************************************************************************	
		
	def index_finder(self,digit = "", index = 0 , weight = 0):
		counter = 0
			 
		if digit > 0:
			for i in range(1 * pow(10,weight), digit + pow(10,weight), pow(10,weight)):
				counter += 1

			if counter > 3:	
				diff = self.symbol_keys[index] - digit
				
				if diff < 0: 
					index = self.index_finder(digit - (3 * pow(10,weight)),index+1, weight)	
				else:		
					index = self.index_finder(digit - (3 * pow(10,weight)),index, weight)	
		return index	

		
	#********************************************************************************************
	# First Order For Units Conversion
	#********************************************************************************************
		
	def first_order(self,digit = ""):
		string = ""
		
		xx = self.index_finder(digit, 0)
		
		if xx > 0: 
			if digit - self.symbol_keys[xx] < 0:
				string = (self.major_symbols_dict[self.symbol_keys[0]] * ((digit - self.symbol_keys[xx]) * -1)) + self.major_symbols_dict[self.symbol_keys[xx]]
			else:
				string = self.major_symbols_dict[self.symbol_keys[xx]] + (self.major_symbols_dict[self.symbol_keys[0]] * (digit - self.symbol_keys[xx]))
		else:
			string = self.major_symbols_dict[self.symbol_keys[xx]] * (digit - xx)
		return string

	
	#********************************************************************************************
	# Second Order For Tens and Higher Place Value Conversions
	#********************************************************************************************	
		
	def second_order(self,digit = "", weight = 1):
		
		string = ""
		 
		if digit in self.symbol_keys:
			string = self.major_symbols_dict[digit]
		else:
		
			if digit > 0:
				# for 10s
				if weight == 1:
					xx = self.index_finder(digit, 2 , weight)
					
					if xx > 0: 
						if digit - self.symbol_keys[xx] < 0:
							string = (self.major_symbols_dict[self.symbol_keys[2]] * ((digit - self.symbol_keys[xx]) / -10)) + self.major_symbols_dict[self.symbol_keys[xx]]
						else:
							string = self.major_symbols_dict[self.symbol_keys[xx]] + (self.major_symbols_dict[self.symbol_keys[2]] * ((digit - self.symbol_keys[xx]) / 10))
					else:
						string = self.major_symbols_dict[self.symbol_keys[xx]] * (digit - xx)
			
				# for 100s
				if weight == 2:
					xx = self.index_finder(digit, 4 , weight)
					
					if xx > 0: 
						if digit - self.symbol_keys[xx] < 0:
							string = (self.major_symbols_dict[self.symbol_keys[4]] * ((digit - self.symbol_keys[xx]) / -100)) + self.major_symbols_dict[self.symbol_keys[xx]]
						else:
							string = self.major_symbols_dict[self.symbol_keys[xx]] + (self.major_symbols_dict[self.symbol_keys[4]] * ((digit - self.symbol_keys[xx]) / 100))
					else:
						string = self.major_symbols_dict[self.symbol_keys[xx]] * (digit - xx)
				
				# for 1000s
				if weight == 3:
					string = self.major_symbols_dict[self.symbol_keys[6]] * (digit/1000)
					
		return string

		


dd = RomanNumericals()

with open(sys.argv[1], 'r') as test_cases:
	for test in test_cases:
		test = test.replace("\r\n","").strip()
		if int(test) >= 1 and int(test) <=  3999: 
			print dd.divider(int(test))
		
		