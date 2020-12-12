import turtle as t
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        t_i = t.Turtle("square")
        t_i.color("white")
        t_i.penup()
        t_i.goto(position)
        self.all_turtles.append(t_i)

    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def move(self):
        for seg_num in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg_num - 1].xcor()
            new_y = self.all_turtles[seg_num - 1].ycor()
            self.all_turtles[seg_num].goto(new_x, new_y)

        self.all_turtles[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.all_turtles[0].heading() != DOWN:
            self.all_turtles[0].setheading(UP)

    def down(self):
        if self.all_turtles[0].heading() != UP:
            self.all_turtles[0].setheading(DOWN)

    def left(self):
        if self.all_turtles[0].heading() != RIGHT:
            self.all_turtles[0].setheading(LEFT)

    def right(self):
        if self.all_turtles[0].heading() != LEFT:
            self.all_turtles[0].setheading(RIGHT)
