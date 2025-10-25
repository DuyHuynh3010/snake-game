from turtle import Turtle
from collections import deque
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head=self.segments[0]
        self.direction_queue=deque()



    def create_snake(self):
        starting_position=[(0,0),(-20,0),(-40,0)]
        for position in starting_position:
            self.add_segments(position)

    def add_segments(self,position):
        tim = Turtle()
        tim.shape("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def expand(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        if self.direction_queue:
            new_heading=self.direction_queue.popleft()
            self.snake_head.setheading(new_heading)
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.snake_head.forward(20)

    def up(self):
        if self.snake_head.heading() != 270:
            self.direction_queue.append(90)

    def down(self):
        if self.snake_head.heading() != 90:
            self.direction_queue.append(270)

    def left(self):
        if self.snake_head.heading() != 0:
            self.direction_queue.append(180)

    def right(self):
        if self.snake_head.heading() != 180:
            self.direction_queue.append(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head=self.segments[0]