from turtle import Turtle, Screen
screen = Screen()

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in starting_positions:
            self.add_segment(position)
        screen.update()

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].seth(90)
            self.move()

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].seth(270)
            self.move()

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].seth(180)
            self.move()

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].seth(0)
            self.move()
