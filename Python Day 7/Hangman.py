import random
import hangman_words
import hangman_art
print(hangman_art.logo)
print("Welcome to hangman!")
chosen_word = random.choice(hangman_words.word_list)

place_holder = ""
for x in range(len(chosen_word)):
    place_holder += "_ "

print(f"Here's a hint:\n{place_holder}")

guess = ""
display = []
lives = 6
wrong_guess_counter = 6
guess_list = []
while not lives == 0:
    print(f"List of guesses: {guess_list}")
    #This first block is just for the guess variable
    while True:
        last_input = input("Guess a letter").lower().strip()
        if len(last_input) == 1 and last_input.isalpha():
            guess = last_input
            pass
        else:
            print("Enter one letter please.")
            continue
        if guess in guess_list:
            print("You've already guessed this letter!")
            if lives> 0 :
                print(f"You still have {lives} lives! Guess again!")
                break
            else:
                if lives == 1:
                    print(f"You have one life left! Make it count!")
                    break
            continue

        else:
            guess_list.append(guess)
            break
    #First loop for display
    if len(display) == 0:
        for letter in chosen_word:
            if guess == letter:
                display += guess
            else:
                display += "_"
        #This checks to see if any characters in the loop is a letter, if none are -1 life and continue the loop
        contains_alpha = any(any(char.isalpha() for char in string) for string in display)
        if contains_alpha:
            pass
        else:
            print("You didn't guess any letter in the word!. You lost a life. Try again!")
            lives -= 1
            wrong_guess_counter -= 1
            print(f"Lives left : {lives}")
            print(hangman_art.stages[wrong_guess_counter])
            continue

        print(display)
    #All the other loops, this block replaces _ with the guess at the right position if they guessed right
    else:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
                print("You guessed a letter!")
        print(display)

        if guess not in chosen_word:
            print("You guessed no letter from the word!. You lost a life.")
            lives -= 1
            wrong_guess_counter -= 1
            if lives > 1 :
                print(f"You still have {lives} lives")
            elif lives == 1:
                print(f"You have {lives} life left")
            else:
                print(f"No more lives")
            print(hangman_art.stages[wrong_guess_counter])
    #If no more "_" in display and lives != 0 , break and print you one the game!
    if "_" not in display and lives != 0:
        print("You won!")
        break

if lives == 0:
    print("You lost try again!")


