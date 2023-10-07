from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        # to change the shape
        self.shape("turtle")
        # to avoid the misbehaviour of the pen
        self.penup()
        # get it to the starting position and get it to the north direction
        self.go_to_start()
        #setting the head to the direction
        self.setheading(90)

    # creating the new function called go_up
    def go_up(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(0, -280)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False
