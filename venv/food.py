from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randX = random.randint(-280, 280)
        randY = random.randint(-280, 280)
        self.goto(randX, randY)