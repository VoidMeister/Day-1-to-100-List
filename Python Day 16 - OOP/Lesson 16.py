# from turtle import Turtle , Screen
# import module1
# print(module1.another_variable)
#
# zi = Turtle()
# '''ZI is the object and Turtle() is the class'''
# print(zi)
# zi.shape("turtle")
# zi.color("CadetBlue2")
# zi.forward(100)
# '''zi is the OBJECT AND forward is the method'''
# my_screen = Screen()
# print(my_screen.canvheight)
# '''my_screen is the OBJECT and canvheight is the attribute'''
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "l"
print(table)

