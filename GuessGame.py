import random

print ("🎲Welcome To Number Guessing Game🎲")

number = random.randint(1,10) #Computer Guess Number Between 1 to 10
guess = 0

while guess != number:
	guess = int(input("Choose Number Between 1 to 10 :"))

	if guess < number:
		print ("Too Low! Try Again.")
	
	elif guess > number:
		print ("Too High! Try Again.")

	else:
		print ("Hurray! You Won The Game.")	
