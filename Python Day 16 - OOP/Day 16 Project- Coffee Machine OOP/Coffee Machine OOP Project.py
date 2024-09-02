from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_on = True
#FIRST STEP AFTER CREATING CLASSES IS TO DETERMINE THE OBJECTS RELATED TO THOSE CLASSES(
# Ex: What can the money_machine do? Everything from the MoneyMachine() CLASS)
#Makes money_machine the OBJECT of MoneyMachine CLASS
money_machine = MoneyMachine()
#Make coffee_maker the OBJECT of the CoffeMaker CLASS
coffee_maker = CoffeeMaker()
#Makes menu the OBJECT of the Menu CLASS
menu = Menu()

while is_on:
    #Asks the user for a choice
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    #Turns the machine off
    if choice == "off":
        is_on = False
    #Gives a report of the ingredients left and the money
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        #Makes drink the name ATTRIBUTE from the menu OBJECT in MenuItem CLASS
        drink = menu.find_drink(choice)
        #coffee_maker OBJECT calls is_resource_sufficient METHOD, money_machine OBJECT calls make.payment METHOD, and
        # drink.cost calls the COST attribute of the NAME attribute from Menu CLASS
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)


#RECAP :
# TO USE A CLASS
# Assign an OBJECT to the class
# To use a METHOD from that class :
# OBJECT.METHOD(variable/attribute)
# To call an attribute :
# object.attribute or to change attribute --> object.attribute = "asdasd"



