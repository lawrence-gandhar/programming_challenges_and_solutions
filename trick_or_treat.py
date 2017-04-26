# vampire gets 3 candies from one house, zombie 4 candies, and witch 5 candies.
# print number of candies that each child will get. 
# If the number is not integer, round it to the lower: for example, if the resulting number is 13.666, round it to 13.


import sys

with open(sys.argv[1], 'r') as test_cases:
	for row in test_cases:
		row = row.replace("\r\n","").replace("Vampires: ","").replace("Zombies: ","").replace("Witches: ","").replace("Houses: ","").strip().split(",")
		
		Vampires = 3 * int(row[0]) * int(row[3]) 
		Zombies = 4 *  int(row[1]) * int(row[3])
		Witches = 5 * int(row[2]) * int(row[3])
		
		candy_collected = int((Vampires + Zombies + Witches)/(int(row[0]) + int(row[1]) + int(row[2])))
		
		print candy_collected
		