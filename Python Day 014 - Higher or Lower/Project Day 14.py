import random
import game_data
import art

def compare(person):
    global current_score
    if person_a["follower_count"] > person_b["follower_count"] and person == "A":
        current_score += 1
        return True
    elif person_a["follower_count"] < person_b["follower_count"] and person == "A":
        print(f"You lose! Current score: {current_score}")
        return False
    elif person_a["follower_count"] < person_b["follower_count"] and person == "B":
        current_score += 1
        return True
    elif person_a["follower_count"] > person_b["follower_count"] and person == "B":
        print(f"You lose! You scored {current_score} points.")
        return False

current_score = 0

print(art.logo)
##Random dictionary/person from data
while True:
    person_a = random.choice(game_data.data)
    person_b = random.choice(game_data.data)
    if person_a == person_b:
        continue
    else:
        break
#Compare A and B
while True:
    print(f"Compare A: {person_a["name"]}, a {person_a["description"]} from {person_a["country"]}")
    print(art.vs)
    print(f"Compare B: {person_b["name"]}, a {person_b["description"]} from {person_b["country"]}")
    #Input A or B
    while True:
        choice = input("Who has more followers? Type A or B: ").title().strip()
        if choice == "A" or choice =="B":
            break
        else:
            print("Enter the right input r word.")
            continue
    #If not right choice - lose
    if not compare(choice):
        break
    #Set the right answer as person a
    higher_value = {}
    if person_a["follower_count"] > person_b["follower_count"]:
        higher_value = person_a
    else:
        higher_value = person_b
    person_a = higher_value
    while True:
        person_b = random.choice(game_data.data)
        if person_a == person_b:
            continue
        else:
            break
