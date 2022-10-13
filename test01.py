
# First, we need to import the 'random' module.
# This module contains the functionality we need to be able to randomly select the winning number.

import random

# Now, we need to select a random number.
# This line will set the variable 'correct' to be equal to a random integer between 1 and 10.

correct = random.randint(1, 10)

# Let's get the user's first guess using the 'input' function.

guess = input("Enter your guess: ")

# Right now, the user's input is formatted as a string.
# We can format it as an integer using the 'int' function.

guess = int(guess)

# Let's start a loop that will continue until the user has guessed correctly.
# We can use the '!=' operator to mean 'not equal'.

while guess != correct:
	
	# Everything in this loop will repeat until the user has guessed correctly.
	# Let's start by giving the user feedback on their guess. We can do this using the 'if' statement.
	
	# This statement will check if a comparison is true.
	# If it is, the code inside the 'if' statement will run.
	
	if guess > correct:
		
		# This code will run if the user guessed too high.
		# We can show a message to the user using the 'print' function.
		
		print("You've guessed too high. Try guessing lower.")
	
	else:
		
		# The 'else' statement adds on to an 'if' statement.
		# It will run if the condition of the 'if' statement is false.
		
		# In this case, it will run if the user guessed too low, so we can give them feedback.
		
		print("You've guessed too low. Try guessing higher.")
	
	# Now we need to let the user guess again.
	# Notice how I am combining the two lines of guessing code to make just one line.
	
	guess = int(input("Enter your guess: "))

# If a user's guess is still incorrect, the code in the 'while' loop will be repeated.
# If they've reached this point in the code, it means they guessed correctly, so let's say that.

print("Congratulations! You've guessed correctly.")

