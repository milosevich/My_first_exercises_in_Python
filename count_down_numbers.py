# Define a variable and set it to the integer number of 10000
# Use a while loop to count down this number until it reaches 0
# Each iteration of the loop must decrease the number by a value of 100 thru 10, repeat this if we have not reached zero
# Display each new value of the variable
# When the variable reaches zero or goes below zero the program will end
# Never let a negative value display to the user
x = 10000
x = int (x)
i = 100
i = int (i)
print (x)
while x >= 0:
	if (i < 10):
		i = 100
	x = x - i	
	i = i - 1
	if x < 0:
		continue
	print (x)
print ("End")