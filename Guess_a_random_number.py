# importing the random module
import random
# Greetings
print("Welcome to the Guess the Number Game!")
print("I've selected a random number between 1 and 100.")
print("You have 5 attempts to guess it.")
print("\n")
# Select random number
rad_num=random.randint(1,100)
print(rad_num)
# Repeatedly prompt the player for guesses until they guess correctly
for x in range(1,6):
    guess_num=int(input(f"Guess the number (attempt {x}): "))
    if guess_num < rad_num:
        print("Too low! Try again.")
        continue
    elif guess_num > rad_num:
        print("Too high! Try again.")
        continue
    else:
        print(f"Congratulations! You guessed the number {rad_num} in {x} attempts")
        break
