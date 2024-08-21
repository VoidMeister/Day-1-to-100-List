# Dungeon Game
dungeon =  r"""
_________________________________________________________
 /|     -_-                                             _-  |\
/ |_-_- _                                         -_- _-   -| \
  |                            _-  _--                      |
  |                            ,                            |
  |      .-'````````'.        '(`        .-'```````'-.      |
  |    .` |           `.      `)'      .` |           `.    |
  |   /   |   ()        \      U      /   |    ()       \   |
  |  |    |    ;         | o   T   o |    |    ;         |  |
  |  |    |     ;        |  .  |  .  |    |    ;         |  |
  |  |    |     ;        |   . | .   |    |    ;         |  |
  |  |    |     ;        |    .|.    |    |    ;         |  |
  |  |    |____;_________|     |     |    |____;_________|  |
  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  |
  |  |  / __  ()        -|        -  |  /  __--      -®   |  |
  |  | /        __-- _   |   _- _ -  | /        __--_    |  |
  |__|/__________________|___________|/__________________|__|
 /                                             _ -        lc \
/   -_- _ -             _- _---                       -_-  -_ \
"""
three_doors = r'''
   ______________             
|\ ___________ /|           
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| Yellow  
______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| Blue

 ______________
|\ ___________ /|
| |  /|,| |   | |
| | |,x,| |   | |
| | |,x,' |   | |
| | |,x   ,   | |
| | |/    |%==| |
| |    /] ,   | |
| |   [/ ()   | |
| |       |   | |
| |       |   | |
| |       |   | |
| |      ,'   | |
| |   ,'      | |
|_|,'_________|_| Red
'''
print(dungeon)
print("Welcome to treasure island.")
print("Your mission is to find treasure.")

while True:
    while True:
        door_choice = input("Choose the right or the left door.")
        if not door_choice.lower().strip() == "right" and not door_choice.lower().strip() == "left":
            print("Invalid input. Try again")
            continue
        else:
            break
    if door_choice.lower().strip() == "right":
       pass
    elif door_choice.lower().strip() == "left":
        print("Your mom was waiting behind the door with your report card.(She saw ONE B).\nYou died.")
        continue
    else:
        print("Enter a valid choice")
        continue

    while True:
        swim_wait = input("Are you going to swim across or wait for the boat? Write Swim to swim or Boat to wait for the boat")
        if not swim_wait.lower().strip() == "boat" and not swim_wait.lower().strip() == "swim":
            print("Invalid input. Try again")
            continue
        else:
            break
    if swim_wait.lower().strip() == "boat":
        pass
    else:
        print("A trout ate your wewe. You died")
        continue
    print(three_doors)

    while True:
        final_door = input("Choose the final door.")
        if not final_door.lower().strip() == "blue" and not final_door.lower().strip() == "yellow" and not final_door.lower().strip() == "red":
            print("Invalid input")
            continue
        else:
            break
    if final_door.lower().strip() == "blue":
        print("You got vaporized by an alien")
        continue
    elif final_door.lower().strip() == "red":
        print("Your girlfriend was waiting behind the door.(She found the texts with side hoe)")
        continue
    else:
        break

print("You found the treasure!")





