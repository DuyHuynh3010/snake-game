from turtle import Screen
from score_board import Scoreboard
import time

from snake import Snake
from food import Food

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Duy's Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
score_board=Scoreboard()

screen.listen()
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")

game_status=True
while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_head.distance(food)<15:
        food.refresh()
        snake.expand()
        score_board.clear()
        score_board.increase_score()

    if snake.snake_head.xcor()>290 or snake.snake_head.xcor()<-290 or snake.snake_head.ycor()>290 or snake.snake_head.ycor()<-290:
        game_status = False
        score_board.gameover()


    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment)<10:
            score_board.gameover()
            game_status=False



screen.exitonclick()



