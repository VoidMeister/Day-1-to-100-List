import art
#First print the gavel
print(art.logo)
print("Welcome to the silent auction")
last_name = False
bidders = {}
while not last_name:
    name = input("What is your name?Enter your first and last name.")
    bid = float(input("Enter bid amount."))
    bidders[name] = bid
    is_last_person = input("Is this the last person? Enter yes or no").strip().lower()
    if is_last_person == "yes":
        last_name = True
        print("\n" * 50)
    else:
        print("\n" * 50)
        continue

# keep track of current highest bidder and bid
highest_bid = 0
highest_bidder = ""
"""
{ 
"name1": 10,
"name2": 16,
"name3": 13,
}
"""
for key in bidders:
    # get the bid of the current key
    bid = bidders[key]
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = key

print(f"{highest_bidder} has won the bid with ${highest_bid}")

