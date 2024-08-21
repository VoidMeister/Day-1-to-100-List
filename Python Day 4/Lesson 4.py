#Randomisation
import random
import Lesson_4_module
random_integer = random.randint(1, 10)

print(random_integer)
print(Lesson_4_module.my_favorite_number)

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

#Quiz print Heads or Tails depending on the generated number
#could have also used
# random.randint(0,1)
heads_or_tails = random.uniform(1,10)
if heads_or_tails < 6:
    print("Tails")
else:
    print("Heads")
# Lists
fruits = ["Apple", "Pear", "Banana", "Peach"]

print(fruits[0])#Going to print out Apple
print(fruits[-1])#Going to print out Peach
fruits[2] = "Grapes" # Changes Banana into Grape
fruits.append("Orange")#Added Orange to the list
print(fruits)
fruits.extend(["Dragonfruit", "Kiwi"])# Add multiple items to the list
#List data structures can be found on python website

#Lists can be in lists

fruits = ["Strawberries", "Apples", "Grapes","Oranges"]
vegetables = ["Tomatoes", "Carrots", "Cucumber"]

healthy_food = [fruits, vegetables]
print(healthy_food)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])
print(dirty_dozen[0])
print(dirty_dozen[1])
print(dirty_dozen[1][2])
print(dirty_dozen[1][3])



