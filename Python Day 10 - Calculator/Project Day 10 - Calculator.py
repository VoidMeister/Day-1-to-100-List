import art

def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2


operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,


}
print(art.logo)
# If a string contains one period.
# If a string does not contain any other characters except numbers.
def is_float(string):
    period_counter = 0

    for character in string:
        if not character.isdigit() and not character == ".":
            return False
        if character == ".":
            period_counter += 1
    if period_counter > 1 or len(string) <= 1:
        return False
    # if i made it here it means that the two conditions are checked
    return True

while True:
    while True:
        # This block asks for the first number
        num1 = input("Enter the first number").strip()
        if is_float(num1):
            num1 = float(num1)
            break
        else:
            print("Enter a valid input.")
            continue
    while True:
        #This block asks for the operator
        while True:
            operator = input("Enter an operator. + to add, - to subtract, * to multiply, and / to divide").strip()
            if operator == "+" or operator == "-" or operator == "/" or operator == "*":
                break
            else:
                print("Enter a valid input.")
                continue
        #This block asks for the second input
        while True:
            num2 = input("Enter the second number.").strip()
            if is_float(num2):
                num2 = float(num2)
                break
            else:
                print("Enter a valid input.")
        #This block computes the two numbers
        try:
            output = operations[operator](num1,num2)
        except ZeroDivisionError:
            print("You cant divide by 0 you retard.")
            break
        print(f"The result is {output}")
        #Asks if tey want to continue
        while True:
            again = input("Would you like to continue? Type yes or no").strip().title()
            if again == "Yes" or again == "No":
                break
            else:
                "Please enter a valid input."
        if again == "Yes":
            num1 = output
            continue
        else:
            break





