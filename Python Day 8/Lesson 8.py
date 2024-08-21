# 1 usage
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Angela")

#Functions with more than one input
def greet_with(name,location):
    print(f"Hello {name}.")
    print(f"What is it like to live in {location}?")

greet_with(name="alex",location="Canada")


def calculate_love_score(name1, name2):
    TRUE = 0
    LOVE = 0

    for i in name1:
        if i == "t" or i == "r" or i == "u" or i == "e":
            TRUE += 1
    for i in name2:
        if i == "t" or i == "r" or i == "u" or i == "e":
            TRUE += 1
    for i in name1:
        if i == "l" or i == "o" or i == "v" or i == "e":
            LOVE += 1
    for i in name2:
        if i == "l" or i == "o" or i == "v" or i == "e":
            LOVE += 1
    print(f"Love score = {TRUE}{LOVE}")

nameone = input("What's the first name?")
nametwo = input("What's the second name?")
calculate_love_score(name1=nameone, name2=nametwo)
