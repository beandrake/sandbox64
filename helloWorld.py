### What is this, some sort of test file? :O

def recurseForUsers(hiya):
	hi = hiya[0:1]
	ya = hiya[1:]
	
	ya = ya if ya == "" else recurseForUsers(ya)	
	return hi + ya


if __name__ == "__main__":

	greeting = "Hello World"

	salutation = ""

	while len(greeting) > 0:
		lastLetter = greeting[-1]
		salutation = lastLetter + salutation
		greeting = greeting[0:-1]

	hiya = recurseForUsers(salutation)

	for letter in hiya:
		print(letter, end="")

	print()



