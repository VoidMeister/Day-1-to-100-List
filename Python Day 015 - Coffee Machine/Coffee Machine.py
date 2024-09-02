import time

resources = {
    "Water" : 1000,  # in ml
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
espresso_available = True
latte_available = True
cappuccino_available = True

def vending_machine():
    global resources
    global coffee_proportions
    global availability
    global espresso_available
    global latte_available
    global cappuccino_available
    availability = {
        "Espresso": espresso_available,
        "Latte": latte_available,
        "Cappuccino": cappuccino_available,
    }

    for ingredient_key in resources:
        try:
            if ingredient_key in coffee_proportions[choice]:
                if resources[ingredient_key] < coffee_proportions[choice][ingredient_key]:
                    availability[choice] = False

        except NameError:
            if ingredient_key in coffee_proportions["Espresso"]:
                if resources[ingredient_key] < coffee_proportions["Espresso"][ingredient_key]:
                    availability["Espresso"] = False
                    espresso_available = availability["Espresso"]
            if ingredient_key in coffee_proportions["Latte"]:
                if resources[ingredient_key] < coffee_proportions["Latte"][ingredient_key]:
                    availability["Latte"] = False
                    latte_available = availability["Latte"]
            if ingredient_key in coffee_proportions["Cappuccino"]:
                if resources[ingredient_key] < coffee_proportions["Cappuccino"][ingredient_key]:
                    availability["Cappuccino"] = False
                    cappuccino_available = availability["Cappuccino"]
        except KeyError:
            pass
    espresso_status = "✔" if availability["Espresso"] else "X"
    latte_status = "✔" if availability["Latte"] else "X"
    cappuccino_status = "✔" if availability["Cappuccino"] else "X"

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


def output(decision):
#choices : ["Espresso","Latte", " Cappuccino", "Off", "Resources"]
    if decision == "Off":
        print("Machine will turn off in 5 seconds.")
        time.sleep(5)
        return False
    elif decision == "Resources":
        print(resources)
        time.sleep(5)
def ask_change():
    #Ask the user to put in change
    global resources
    money_counter = 0
    while coffee_proportions[choice]["Cost"] > money_counter:
        print(f"You owe {coffee_proportions[choice]["Cost"] - money_counter}$ ")
        money_given = input("Enter money. Enter 1 currency at a time. Penny, Nickel, Dime, and Quarter)")
        if money_given in ["Penny", "Nickel", "Dime", "Quarter"]:
            if money_given == "Penny":
                money_counter += 0.01
            if money_given == "Nickel":
                money_counter += 0.05
            if money_given == "Dime":
                money_counter += 0.10
            if money_given == "Quarter":
                money_counter += 0.25
    if coffee_proportions[choice]["Cost"]< money_counter:
        change = money_counter - coffee_proportions[choice]["Cost"]
        print(f"Here's {change} back")
    resources["Money"] += coffee_proportions[choice]["Cost"]



coffee_machine_status = True
while coffee_machine_status:
    global availability
    vending_machine()
    while True:
        choice = input("Choose a drink.").strip().title()
        if choice in ["Espresso","Latte", "Cappuccino", "Off", "Resources"]:
            break
        else:
            print("Enter a valid input...")

#CHECK : print(choice) VALID
#CHECK : Test turning off coffee machine VALID
    #Also calls the output function
    if choice == "Off":
        coffee_machine_status = output(choice)
        continue
    elif choice == "Resources":
        output(choice)
        continue
    if availability[choice]:
        #Make coffe
        ask_change()
        #Remove resources
        for ingredient_key in resources:
            if ingredient_key in coffee_proportions[choice]:
                resources[ingredient_key] -= coffee_proportions[choice][ingredient_key]
        print("Here's your coffee!")
        continue
    else:
        print("Sorry, we ran out!")
        continue