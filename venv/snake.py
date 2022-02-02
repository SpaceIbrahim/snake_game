from turtle import Turtle, Screen
screen = Screen()
screen.tracer(0)
START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segment = []
        self.initialize()
        self.head = self.segment[0]


    def initialize(self):
        for position in START_POS:
            sg = Turtle("square")
            sg.penup()
            sg.color("white", "white")
            sg.goto(position)
            self.segment.append(sg)


    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            newX = self.segment[seg_num - 1].xcor()
            newY = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(newX, newY)

        self.head.forward(MOVE_DIST)


    def moveUp(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def moveLeft(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


    def moveRight(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def moveDown(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def new(self):
        newX = self.segment[-1].xcor()
        newY = self.segment[-1].ycor()
        sg = Turtle("square")
        sg.penup()
        sg.color("white", "white")
        sg.goto(x=newX, y=newY)
        self.segment.append(sg)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000,1000)
        self.segment.clear()
        self.initialize()
        self.head = self.segment[0]