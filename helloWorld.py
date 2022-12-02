### What is this, some sort of test file? :O
import sys
DEFAULT_GREETING = "Hello World"


def recurseForUsers(hiya):
	hi = hiya[0:1]
	ya = hiya[1:]
	
	ya = ya if ya == "" else recurseForUsers(ya)	
	return hi + ya


if __name__ == "__main__":

	# Let the user customize their greeting; it's all about personal choice
	if len(sys.argv) > 1:
		greeting = sys.argv[1] 
	else:
		greeting = DEFAULT_GREETING
	
	# Very important things happening here, pretty sure this is super necessary
	salutation = ""
	while len(greeting) > 0:
		lastLetter = greeting[-1]
		salutation = lastLetter + salutation
		greeting = greeting[0:-1]

	# This is where the recursion happens
	hiya = recurseForUsers(salutation)

	# Printing a string, like you do
	for letter in hiya:
		print(letter, end="")

	# Fence-posting!
	print()



