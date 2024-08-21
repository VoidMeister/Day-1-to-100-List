#1. Ask how many letters would you like the password
#2. ask How many symbols in the password
#3  ask how many number in the password
import random
letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+",
    "-", "=", "{", "}", "[", "]", "|", ":", ";", "'", "<", ">", ",", ".", "/", "?"
]
print("Welcome to the password generator!")
while True:
    nr_letters = input("How many letters would you like in the password\n").strip()
    if nr_letters.isdigit():
        nr_letters = int(nr_letters)
        break
    else:
        print("Enter a valid number.")
        continue
while True:
    nr_numbers = input("How many numbers would you like in the password\n").strip()
    if nr_numbers.isdigit():
        nr_numbers = int(nr_numbers)
        break
    else:
        print("Enter a valid number.")
        continue
while True:
    nr_symbols = input("How many symbols would you like in the password\n").strip()
    if nr_symbols.isdigit():
        nr_symbols = int(nr_symbols)
        break
    else:
        print("Enter a valid number.")
        continue
#Extract x number of str from symbols,numbers,letters
list_letters = []
for i in range(1,(nr_letters + 1 )):
    list_letters.append(random.choice(letters))
list_numbers = []
for i in range(1,(nr_numbers + 1)):
    list_numbers.append(random.choice(numbers))
list_symbols = []
for i in range(1, (nr_symbols + 1)):
    list_symbols.append(random.choice(symbols))
list_characters = list_letters + list_numbers + list_symbols
print(list_characters)
print(f"Your new password is: ")
random.shuffle(list_characters)
print("".join(list_characters))

