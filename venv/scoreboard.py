from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        data = open("E.txt")
        self.highscore = int(data.read())
        data.close
        self.hideturtle()
        self.color("white")
        self.goto(-1, 250)
        self.score = 0
        self.displayscore()

    def displayscore(self):

        self.clear()
        if self.highscore < self.score:
            self.highscore = self.score
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=("Courir", 18, "normal"))

    def updatescore(self):
        self.score += 1
        self.displayscore()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!!", False, align="center", font=("Courir", 18, "normal"))

    def reset(self):
        self.score = 0
        self.displayscore()
        with open("E.txt",mode="w") as file:
            file.write(f"{self.highscore}")