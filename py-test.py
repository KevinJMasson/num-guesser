import random

def validNum(inp):
	if inp > 0 and inp <= 100:
		return True
	else:
		return False

def match(inp):
	if inp == num:
		return True
	else:
		return False

def highLow(inp):
	if inp > num:
		return "Higher"
	else:
		return "Lower"

num = random.randint(1,100)
guesses = 5

user = int(input("Guess a number between 1 and 100: "))

while validNum(user) == False:
	print("Please input a valid number between 1 and 100")
	user = int(input("Guess a number between 1 and 100: "))

while match(user) == False and guesses > 0:
	guesses = guesses - 1
	if guesses == 0:
		break
	print("Your number is " + highLow(user)  + " than the number")
	print("You have " + str(guesses) + " guesses left")
	user = int(input("Guess a new number between 1 and 100: "))

if guesses > 0:
	print("Congratulations! The number was " + str(num) + "!")
else:
	print("You are out of guesses!")

