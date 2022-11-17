### What is this, some sort of test file? :O

greeting = "Hello World"

salutation = ''

while len(greeting) > 0:
	lastLetter = greeting[-1]
	salutation = lastLetter + salutation
	greeting = greeting[0:-1]

for letter in salutation:
	print(letter, end='')

print()



