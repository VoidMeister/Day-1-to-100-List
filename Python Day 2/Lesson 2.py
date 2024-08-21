#Subscripting
print("Hello"[-1])

#Integer are whole numbes
print(12_3+3_45)

#Larger integers
print(123_345_567)

#float
print(123.123)

#Boolean
True
False

#Print the data type
print(type(True))

# Converting string into int
print(int("123")+int("456"))

#Example of application
name_of_user = input("Enter your name: ")
length_of_name = len(name_of_user)

print("Your name length is " + str(length_of_name))

#Operators
print(1 + 1)
print(7 - 3)
print(8 / 2)
print(8 // 2)
print(8 ** 5)
print(3 * 3 + 3 / 3 - 3 )

#BMI Quiz

height = 1.65
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
input_weight = input("Enter your weight in kg: ")
input_height = input("Enter your height in meters: ")

bmi = int(input_weight) / (float(input_height)**2)

print(round(bmi, 2))

score = 0
score += 1
print(score)

#f-strings
score = 0
height = 1.87
player_is_winning = True
print(f"Your score is {score}, your height is {height}, your are winning is  {player_is_winning}")