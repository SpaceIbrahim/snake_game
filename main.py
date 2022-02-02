from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()

screen.onkey(snake.moveUp, "Up")
screen.onkey(snake.moveDown, "Down")
screen.onkey(snake.moveLeft, "Left")
screen.onkey(snake.moveRight, "Right")

game = True
while game:
    screen.update()
    time.sleep(0.05)

    snake.move()

    if snake.head.distance(food) < 15:
        print(score.score)
        food.refresh()
        score.updatescore()
        snake.new()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()

