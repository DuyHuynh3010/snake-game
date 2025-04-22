from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align="center",font=("arial",24,"normal"))

    def refresh(self):
        self.clear()


    def increase_score(self):
        self.score+=1
        self.write(f"Score: {self.score}", align="center", font=("arial", 24, "normal"))


    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=("arial", 24, "normal"))