# Rock Paper Scissors game
import random
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors
#Prints your choice
#Prints the computers choice
#Decides who won
#Rock draws Rock, Rock loses to Paper, Paper draws Paper, Paper loses to Scissors, Scissors draws Scissors,
possible_choices = [paper,scissors,rock]

print("Welcome to Rock, Paper, Scissors!")
while True:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.")
    if choice.isdigit():
        choice = int(choice)
        pass
    else:
        print("Enter a valid number")
        continue
    if choice == 1 or choice == 2 or choice == 0:
        break
    else:
        continue

if int(choice) == 0:
    print(rock)
    losing_choice = scissors
elif int(choice) == 1:
    print(paper)
else:
    print(scissors)

print("Computer choice:")

computer_choice = random.choice(possible_choices)

print(computer_choice)


#Rock draws Rock, Rock loses to Paper, Paper draws Paper, Paper loses to Scissors, Scissors draws Scissors,
if computer_choice == rock and choice == 0:
    print("Draw")
elif computer_choice == rock and choice == 1:
    print("You win!")
elif computer_choice == rock and choice == 2:
    print("You lose!")
elif computer_choice == paper and choice == 0:
    print("You lose!")
elif computer_choice == paper and choice == 1:
    print("Draw")
elif computer_choice == paper and choice == 2:
    print("You win!")
elif computer_choice == scissors and choice == 0:
    print("You win!")
elif computer_choice == scissors and choice == 1:
    print("You lose!")
elif computer_choice == scissors and choice == 2:
    print("Draw")

