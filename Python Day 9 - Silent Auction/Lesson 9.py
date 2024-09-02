#Dictionary
#{key : value}
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])
#You can add to dictionaries
programming_dictionary["Alexandru"] = "He is the gayest man alive"

print(programming_dictionary)
#You can empty dictionaries of you want to erase score for example
empty_dictionary = {}
programming_dictionary = {}
print(programming_dictionary)
#You can change keys from dictionaries
programming_dictionary["Alexandru"] = " He heard zi say he likes his mom"

#You can loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}
#Prints out Lille
print( travel_log["France"][1] )
#Prints out D
nest_list = ["A", "B", ["C", "D"]]
print(nest_list[2][1])
#Can store dictionary in a dictionary
travel_logg = {
    "France": {
        "num_time_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"],
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}
print(travel_logg["Germany"]["cities_visited"][2])
