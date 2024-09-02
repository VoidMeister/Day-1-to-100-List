#if else statement
print("Welcome to the rollercoaster!")
height = float(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ticket on us")
    else:
        bill = 12
        print("Adult tickets are $12.")

    while True:
        wants_photo = input("Do you want to have your photo taken? Type y for Yes and n for No.")
        if wants_photo == "y" or wants_photo == "n":
            break
        print("Are you retarded, only y and n.")



    if wants_photo == "y":
        # Add $3 to the bill
        bill += 3

    print(f"Your final bill {bill}")

else:

    print("Sorry you need to grow taller before you can ride.")
#Modulo operator %

#Quiz Even or odd number, ask for input, if input Odd print "odd", else print" "even"
number = float(input("What is your number? "))
if number != int(number):
    print("Number is not even or odd, it is a decimal number")
elif number % 2 == 0:
    print("Number is an even number.")
else:
    print("Number is an odd number.")

#Quiz BMI calculator interpretation

# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
#
# if bmi < 18.5:
#     print("underweight")
# elif bmi >= 25:
#     print("overweight")
# else:
#     print("normal weight")
#

weight = 1000
height = 1.85

bmi = weight / (height**2)
print(bmi)
if bmi < 18.5:
    print("You are anorexic")
elif bmi >= 18.5:
    if bmi < 25:
        print("You are a gigachad")
    else:
        print("You're a fat ass")


#Pizza bill calculator

print("Welcome to Python Pizza!")
while True:
    size = input("What size pizza would you like? Small, Medium or Large?")
    if size == "Small" or size == "Medium" or size == "Large":
        break
while True:
    pepperoni = input("Would you like extra pepperoni? Y or N")
    if pepperoni == "Y" or pepperoni == "N":
        break
while True:
    cheese = input("Would you like extra cheese? Y or N")
    if cheese == "Y" or cheese == "N":
        break
bill = 0

if size == "Small":
    bill += 15
elif size == "Medium":
    bill += 20
else:
#Large
    bill += 25
if pepperoni == "Y":
    if size == "Small":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1


print(f"Your bill is ${bill}")
# if pepperoni == "Y":
#     bill += 2
# else:
#     bill =+ 0
# if cheese == "Y":
#     bill += 1
#extra pepperoni for small pizza +2, medium or large +3
#extra cheese for any size is +1
#smal pizza is 15
#medium pizza is 20
#large pizza is 25


