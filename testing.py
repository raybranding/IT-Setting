import random
# Russian Roulette Code

safe = random.randint(1,6)

guess = int(input("Silly goose, pick a number from 1 to 6! :>"))
if guess == safe:
	print("Congratulations! You're safe. <3")
else:
	print("Aw shucks. Better luck next time!")
