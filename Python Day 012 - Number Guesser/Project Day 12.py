import random
from mimetypes import guess_type

print("Welcome to the Number Guessing Game!\nI'm Thinking of a number between 1 and 100.")
number_of_guesses = 0
number_to_guess = random.randint(1,100)

#####BLOCK 1########Prints welcome, and asks the difficulty that the player wants
def difficulty(diff):
    while True:
        number_guesses = input("Choose a difficulty. Type 'easy' or 'hard':").strip().lower()
        if not number_guesses == "easy" and not number_guesses == "hard":
            print("Enter a valid input.")
            continue
        else:
            break
    if number_guesses == "easy":
        diff = 10
        return diff
    else:
        diff = 5
        return diff

number_of_guesses = difficulty(number_of_guesses)
#####BLOCK 2########
#Asks the user to make a guess
#Check to see if the guess is the right number
guess = "0"
while number_of_guesses != 0 and not int(guess) == number_to_guess:
    while True:
        guess = input("Make a guess:")
        if guess.isdigit() and 0 < int(guess) <= 100:
            break
        else:
            print("Enter a valid input")
            continue

    if int(guess) == number_to_guess:
        print("You guessed the right number!")
        break
    elif int(guess) > number_to_guess:
        number_of_guesses -= 1
        if number_of_guesses > 0:
            print("Too high")
            print(f"You have {number_of_guesses} left.")
        elif number_of_guesses == 0:
            print("You lost!")
    elif int(guess) < number_to_guess:
        number_of_guesses -= 1
        if number_of_guesses > 0:
            print("Too low")
            print(f"You have {number_of_guesses} left.")
        elif number_of_guesses == 0:
            print("You lost!")








