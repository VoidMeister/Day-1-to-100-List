#Russian Roulette for the bill
import random
import time
while True:
    number_of_people = input("Enter number of people participating\n").strip()

    if  number_of_people.isdigit():
        number_of_people = int(number_of_people)
    else:
        print("Enter a valid number")
        continue
    if int(number_of_people) < 1:
        print("Enter a valid number")
        continue
    else:
        break

players_names = []

for i in range(number_of_people):
    name = input(f"Enter the player name {i+1}: ").strip()
    players_names.append(name)

print("Players in the game:")
for name in players_names:
    print(name)

while True:
    ready_or_not = input("Are you ready? Write yes or no")
    if ready_or_not.lower().strip() == "yes":
        break
    elif ready_or_not.lower().strip() == "no":
        continue
    else:
        print("Enter a valid answer")
        continue

time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(f"{random.choice(players_names)} has to pay the bill!")
