from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.highscore=int(data.read())
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(f"score: {self.score} high score: {self.highscore}", align="center", font=("arial", 24, "normal"))

    def refresh(self):
        self.clear()


    def increase_score(self):
        self.score+=1
        self.update_score()

    def update_score(self):
        self.refresh()
        self.write(f"score: {self.score} high score: {self.highscore}", align="center", font=("arial", 24, "normal"))

    def reset_score(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_score()