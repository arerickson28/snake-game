# Create snake body
# Move the snake
# Control snake with keyboard controls
#detect collision with food
#create a scoreboard
#When does game end?
# Detect collision with wall
# Detect collision with self
# Three classes: Snake, food, scoreboard

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on :
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collison
    if snake.head.distance(food) < 15 :
        food.refresh()
        scoreboard.update_score()





screen.exitonclick()