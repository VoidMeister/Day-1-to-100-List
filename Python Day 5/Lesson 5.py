#for loops
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print (fruit + " pie")

student_scores = [14, 45, 75, 56, 79, 95, 1, 35]
total_exam_score = sum(student_scores)

sum = 0

for score in student_scores:
    sum += score

print(sum)
#Prints the largest scores
print(max(student_scores))
#Print the largest number in a list without the max function

student_grades = [1,9,2,8,3,7,4,6,5]
#.sort() could work but not the point of the exercise

max_score = 0
for score in student_grades:
    if score > max_score:
        max_score = score
print(max_score)
#for loops and the range() function

for number in range(1,11):
    print(number)

#Gauss challenge
total = 0
for num in range(1,101):
    total += num
print(total)
#FizzBuzz Challenge
for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        num = str("FizzBuzz")
    elif num % 3 == 0: #and num % 5 != 0:
        num = str("Fizz")
    else:
        if num % 5 == 0: # and num % 3 != 0:
            num = str("Buzz")
    print(num)
