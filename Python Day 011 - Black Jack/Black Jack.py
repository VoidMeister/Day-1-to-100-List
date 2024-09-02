import random
import art
def player_score():
    global player_total
    for card in player_cards:
        if not card == "Ace":
            player_total += (cards[card])
        elif card == "Ace" and player_total <= 10:
            player_total += (cards[card][1])
        else:
            player_total += (cards[card][0])
    return player_total

def dealer_score():
    global dealer_total
    for card in dealer_cards:
        if not card == "Ace":
            dealer_total += (cards[card])
        elif card == "Ace" and dealer_total <= 10:
            dealer_total += (cards[card][1])
        else:
            dealer_total += (cards[card][0])
    return dealer_total

def ask():
    global player_total
#Asks if the player wants to hit, if hits append random card
    while True:
        hit_or_stand = input("Do you want to hit or stand? Type hit or stand.")
        if hit_or_stand == "hit" or hit_or_stand == "stand":
            break
        else:
            print("Type valid input r word")
            continue
    if hit_or_stand == "hit":
        random_card = random.choice(keys)
        player_cards.append(random_card)
        player_total = 0
        player_score()
    return hit_or_stand

def computer_draw():
    global dealer_total
    while dealer_total < 17:
        random_card = random.choice(keys)
        dealer_cards.append(random_card)
        dealer_total = 0
        dealer_score()

def score_compare():
    global dealer_total
    global player_total
    if dealer_total < 22 and dealer_total > player_total:
        print("You lose!")
    elif dealer_total >= 22:
        print("You win!")
    elif dealer_total == 21 and player_total == 21:
        print("Draw")
    else:
        print("You win!")
cards = {
    "Ace" : [1,11],
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "Jack" : 10,
    "King" : 10,
    "Queen" : 10,
}

player_total = 0
dealer_total = 0

while True:
    player_total = 0
    dealer_total = 0
    player_cards = []
    dealer_cards = []
    print(art.logo)
    print("Welcome to blackjack!")
#Player draws two cards
    keys = list(cards.keys())
    for start in range(2):
        random_card = random.choice(keys)
        player_cards.append(random_card)
    print(f"Your cards: {player_cards}, current score = {player_score()}")
    random_card = random.choice(keys)
    dealer_cards.append(random_card)
    print(f"Computer card:{dealer_cards}")
    dealer_score()
    while player_total < 21:
        if ask() == "hit":
            print(f"Your score is{player_total}")
            continue
        else:
            print(f"Your score is{player_total}")
            break

    if player_total > 21:
        print("You lose!")
        while True:
            again = input("Would you like to play again? Type yes or no")
            if not again == "yes" and not again == "no":
                print("enter a valid input r word")
                continue
            else:
                break
        if again == "yes":
            continue
        else:
            break
    computer_draw()
    print(f"The dealer score is {dealer_total}")
    score_compare()
    while True:
        again = input("Would you like to play again? Type yes or no")
        if not again == "yes" and not again == "no":
            print("enter a valid input r word")
            continue
        else:
            break
    if again == "yes":
        continue
    else:
        break