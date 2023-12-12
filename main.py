from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
    
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.new_segment[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score()

    if snake.new_segment[0].xcor() > 280 or snake.new_segment[0].xcor() < -280 or snake.new_segment[0].ycor() > 280 or snake.new_segment[0].ycor() < -280 : 
        scoreboard.reset()
        snake.reset()
    
    for segment in snake.new_segment[1:]:
        
        if snake.new_segment[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    




screen.exitonclick()