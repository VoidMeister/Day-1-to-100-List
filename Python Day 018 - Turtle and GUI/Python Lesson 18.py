import turtle as t
import random
tim = t.Turtle()
tim.color("red")
from turtle import Turtle, Screen
# #Draw a square challenge
# for timmy in range(4):
#     tim.forward(100)
#     tim.right(90)
#

# #Make tim draw a dashed line
# for timmy in range(15):
#     tim.pendown()
#     tim.forward(15)
#     tim.penup()
#     tim.forward(15)

#Draw a triangle, square, pentagon,hexagon,heptagon.octagon,nonagon and decagon DONE
# sides = [3,4,5,6,7,8,9]
# colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']
#
# for num in sides:
#     angle = 360 / num
#     for i in range(num):
#         tim.forward(100)
#         tim.right(angle)
#     tim.color(random.choice(colorList))
#################
# colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']
# def draw_shape(num):
#     angle = 360 / num
#     for i in range(num):
#         tim.forward(100)
#         tim.right(angle)
#
# for nbr_shapes in range(3,11):
#     draw_shape(nbr_shapes)
#     tim.color(random.choice(colorList))
# Random Walk
# colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']
# tim.speed("fastest")
# tim.pensize(15)
# t.colormode(255)
# directions = [0,90,180,270]
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color
#
# for i in range(200):
#     tim.color(random_color())
#     tim.setheading(random.choice(directions))
#     tim.forward(30)
#Draw a spirograph
#First I need tim to turn until facing back right
t.mode("logo")
t.colormode(255)
tim.speed("fastest")
# until heading is 360
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

heading = 0
while heading <= 360:
    tim.color(random_color())
    tim.circle(100)
    heading += 5
    tim.setheading(heading)

screen = t.Screen()
screen.exitonclick()


