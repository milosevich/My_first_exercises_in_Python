# Ask the user for their name
# Ask the user for their current age
# Use a for loop to help you display the users current age and year and increase by 2 during each iteration
# The loop should stop when the users age is 100 or greater
# Complete this question in as few lines as possible (you should not need an if statement or break)

name = input("What\'s your name?: ")
age_str = input("What\'s your age: ")
age = int(age_str)
year = 2019
for age in range (age, 100, 2):
	print("In ", year, name, "is ",age,".")
	year = year + 2
print ("End")
