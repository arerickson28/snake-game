from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :

    def __init__(self) :
        self.turtle_snake = []
        self.create_snake()
        self.head = self.turtle_snake[0]


    def create_snake(self) :
        for position in STARTING_POSITIONS :
            self.add_turtle(position)


    def add_turtle(self, position) :
        new_turtle_seg = Turtle("square")
        new_turtle_seg.color("white")
        new_turtle_seg.penup()
        new_turtle_seg.goto(position)
        self.turtle_snake.append(new_turtle_seg)


    def extend(self) :
        #add new turtle to snake
        self.add_turtle(self.turtle_snake[-1].position())


    def move(self):

        for seg_num in range((len(self.turtle_snake) - 1), 0, -1) :
            new_x = self.turtle_snake[seg_num - 1].xcor()
            new_y = self.turtle_snake[seg_num - 1].ycor()
            self.turtle_snake[seg_num].goto(new_x, new_y)
    
        self.head.forward(MOVE_DISTANCE)


    def up(self) :
        if self.head.heading() != DOWN :
            self.head.setheading(UP)


    def down(self) :
        if self.head.heading() != UP :
            self.head.setheading(DOWN)


    def left(self) :
        if self.head.heading() != RIGHT :
            self.head.setheading(LEFT)


    def right(self) :
        if self.head.heading() != LEFT :
            self.head.setheading(RIGHT)