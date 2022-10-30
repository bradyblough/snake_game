from turtle import Turtle

# constants
STARTING_POSITIONS = [(0, 0,), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# blueprint for snake
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # snake methods\
    def reset(self): # resets snake and clears previous snakes off-screen
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for starting_position in STARTING_POSITIONS:  # for loop that iterates through each tuple to get a position
            self.add_segment(starting_position)

    # adds segment after user scores
    def add_segment(self, starting_position):
        segment = Turtle()
        segment.shape('square')
        segment.color('white')
        segment.penup()
        segment.goto(starting_position)
        self.segments.append(segment)

    def extend(self): # adds segment to snake when user contacts food
        self.add_segment(self.segments[-1].position())

    def move(self):
        # for loop that moves each segment to the previous segments starting position
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    # functions that ensure player cannot move in opposite direction relative to their current direction.
    # Player cannot immediately move right if moving left or move immediately up if moving down.
    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)
