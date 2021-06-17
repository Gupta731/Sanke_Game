import time
from turtle import Screen
from food import Food
from scoreboard import Score
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('Black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.right, key='d')
screen.onkey(fun=snake.left, key='a')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
