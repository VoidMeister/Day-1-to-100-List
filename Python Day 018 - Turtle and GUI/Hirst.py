import turtle as t
from colors import all_colors
import random

class Picasso:
    """
    This class turns the user into the painter and outputs a painting based on the size that they want the
    painting to be
    """
    def __init__(self):

        self.name = input("Enter your name: ").title()# Name of the user
        self.user = t.Turtle() # Converts the user into an object of turtle
        self.size = int(input("Enter dimensions of the painting. (Ex: Input 10--> Size = 10x10) "))
        #size is the dimension of the painting
    def paint(self):
        """
        Prints Hirst painting depending on size attribute and username
        """
        t.colormode(255)
        t.speed("fastest")
        x = 0
        y = 0
        painter = self.user
        for i in range(0,self.size):
            for j in range(0,self.size):
                color = random.choice(all_colors)
                painter.dot(20,color)
                x = i * 50
                y = j * 50
                painter.teleport(x,y)
        print(f"Here's your work of art {self.name}!")

