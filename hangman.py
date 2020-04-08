# ****************************************
# ************* Hang-Man *****************
# ****************************************


#Generate a random word
rand_word="hello"


# Convert the rand_word to a list and sort it.
rand_list = (list(rand_word))
rand_list.sort()
print(rand_list)


# Keep track of attempts made by the user
attempt=6

# Keep the user from entering invalid values as guesses
def validate_guess():
	while True:
		guess = input('Enter Letter: ')

		# Make sure the user didn't enter more than one letter
		if (len(guess) > 1):
			print("Only on letter at a time!")
			continue
		elif (len(guess) == 0):
			continue
		return guess


while (attempt >= 1):
	# Get user input (Ask to guess a letter)
	# guess = input('Enter Letter: ')
	guess=validate_guess()

	# Check if the guessed letter is in rand_list
	if guess in rand_list:
		# If the user guessed correct, remove it from rand_list
		try: rand_list.remove(guess)
		except ValueError:print('Unexpected ERROR!')


		# Check if this is another attempt or if user win after this move
		if ((len(rand_list) != 0)):
			print ('You are CORRECT!')
		elif((len(rand_list) == 0)):
			print ('You Win!')


	else:print('Wrong. Try again!')


#	print(rand_list)
	attempt = attempt - 1

	# check if rand_list have any letters left.
	if (len(rand_list) == 0):
		break
