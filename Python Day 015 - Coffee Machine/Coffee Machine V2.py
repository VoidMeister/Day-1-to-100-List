import time
resources = {
    "Water" : 50,  # in ml
    "Milk" : 500,    # in ml
    "Coffee" : 250,  # in g
    "Money" : 0.00   # in $
}

coffee_proportions = {
    "Espresso": {
        "Water": 50,    # in ml
        "Milk": 0,      # in ml
        "Coffee": 20,   # in grams
        "Cost" : 1.50   # in $
    },
    "Latte": {
        "Water": 50,    # in ml
        "Milk": 150,    # in ml
        "Coffee": 18,   # in grams
        "Cost" : 2.50   # in $
    },
    "Cappuccino": {
        "Water": 50,    # in ml
        "Milk": 100,    # in ml
        "Coffee": 21,   # in grams
        "Cost": 3.00,   # in $
    }
}
coins_to_value = {
    "Penny" : 0.01,
    "Nickel": 0.05,
    "Dime": 0.10,
    "Quarter": 0.25,
    "Dollar": 1.00,
}

espresso = True
latte = True
cappuccino = True
#Ask the user to put in change
def ask_change():
    money_counter = 0
    while coffee_proportions[choice]["Cost"] > money_counter:
        print(f"You owe {coffee_proportions[choice]["Cost"] - money_counter}$ ")
        money_given = input("Enter money. Enter 1 currency at a time. Penny, Nickel, Dime, Quarter, and Dollar").strip().title()
        if money_given in list(coins_to_value.keys()):
            money_counter += coins_to_value[money_given]

    if coffee_proportions[choice]["Cost"]< money_counter:
        change = money_counter - coffee_proportions[choice]["Cost"]
        print(f"Here's {change} back")
    resources["Money"] += coffee_proportions[choice]["Cost"]

#Check to see which drinks can be made
def ingredient_check():
    global espresso
    global latte
    global cappuccino
    for ingredient_key in resources:
        if ingredient_key in coffee_proportions["Espresso"]:
            if resources[ingredient_key] < coffee_proportions["Espresso"][ingredient_key]:
               espresso = False
            if ingredient_key in coffee_proportions["Latte"]:
                if resources[ingredient_key] < coffee_proportions["Latte"][ingredient_key]:
                    latte = False
            if ingredient_key in coffee_proportions["Cappuccino"]:
                if resources[ingredient_key] < coffee_proportions["Cappuccino"][ingredient_key]:
                    cappuccino = False

    espresso_status = "✔" if espresso else "X"
    latte_status = "✔" if latte else "X"
    cappuccino_status = "✔" if cappuccino else "X"

    print(rf"""
           _____________________
          |     COFFEE MACHINE   |
          |   ________________   |
          |  |  Espresso   {espresso_status}  |  |
          |  |  Latte      {latte_status}  |  |
          |  |  Cappuccino {cappuccino_status}  |  |
          |  |________________|  |
          |   ________________   |
          |  |                |  |
          |  | [  ] [  ] [  ] |  |
          |  | [  ] [  ] [  ] |  |
          |  |________________|  |
          |        __||__   []   |
          |       /      \       |
          |      /        \      |
          |      \________/      |
          |______________________|
    """)
coffee_machine_status = True
while coffee_machine_status:
    ingredient_check()
    while True:
        choice = input("Choose a drink.").strip().title()
        if choice in ["Espresso","Latte", "Cappuccino", "Off", "Resources"]:
            break
        else:
            print("Enter a valid input...")
    if choice == "Off":
        print("Machine will turn off in 5 seconds.")
        time.sleep(5)
        coffee_machine_status = False
        continue
    elif choice == "Resources":
        print(resources)
        time.sleep(5)
        continue
    else:
        if choice == "Espresso" and not espresso:
            print("Sorry, we ran out!")
            continue
        if choice == "Latte" and not latte:
            print("Sorry, we ran out!")
            continue
        if choice == "Cappuccino" and not cappuccino:
            print("Sorry, we ran out!")
            continue
    ask_change()
    print("Here's your coffee!")
    for ingredient_key in resources:
        if ingredient_key in coffee_proportions[choice]:
            resources[ingredient_key] -= coffee_proportions[choice][ingredient_key]
    continue



