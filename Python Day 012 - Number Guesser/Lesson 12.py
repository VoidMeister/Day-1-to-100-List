# def increase_enemies():
#     enemies =2
#     print(f"enemies inside function: {enemies}")
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")
#
# #Local Scope
#
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# print(potion_strength)
# #Global Scope
#
# player_health = 10
# def game():
#     def drink_potion():
#         potion_strength =2
#         print(player_health)
#
#     drink_potion()
#
# #There is no Block Scope in Python
# game_level = 10
#
# enemies = ["Skeleton", "Zombie", "Alien"]
# def create_enemy():
#     #Better to define the variable so it can always be accessed even if ts not modified
#     new_enemy = ""
#     if game_level < 5:
#         new_enemy = enemies[0]
#
#     print(new_enemy)

#Modifying Global Scope

enemies = 1

def increase_enemies(enemy):

    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies(enemies)
print(f"enemies outside function: {enemies}")

#Global constants usually are typed in all upper case