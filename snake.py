from turtle import Turtle, Screen

STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANSE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):

        new_segment = Turtle('square')
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
        self.head.forward(MOVE_DISTANSE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    # def right(self):
    #     if self.segments[0].heading() == 270:
    #         self.segments[0].left(90)
    #     if self.segments[0].heading() == 90:
    #         self.segments[0].right(90)
    #     print(self.segments[0].heading())
    #
    # def left(self):
    #     if self.segments[0].heading() == 270:
    #         self.segments[0].right(90)
    #     if self.segments[0].heading() == 90:
    #         self.segments[0].left(90)
    #
    # def up(self):
    #     if self.segments[0].heading() == 0:
    #         self.angle = 90
    #         self.segments[0].left(self.angle)
    #     if self.segments[0].heading() == 180:
    #         self.angle = 90
    #         self.segments[0].right(self.angle)
    #
    # def down(self):
    #     if self.segments[0].heading() == 0:
    #         self.angle = 90
    #         self.segments[0].right(self.angle)
    #     if self.segments[0].heading() == 180:
    #         self.angle = 90
    #         self.segments[0].left(self.angle)