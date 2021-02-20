from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake :

    def __init__(self) :
        self.t_1 = Turtle()
        self.t_2 = Turtle()
        self.t_3 = Turtle()

        self.turtle = [self.t_1, self.t_2, self.t_3]

        for i in range(3) :
            self.turtle[i].shape("square")
            self.turtle[i].color("white")
            self.turtle[i].penup()
            self.turtle[i].goto((i*(-20)), 0)
        
        self.head = self.turtle[0]


    def move(self):

        for t_num in range((len(self.turtle) - 1), 0, -1) :
            new_x = self.turtle[t_num - 1].xcor()
            new_y = self.turtle[t_num - 1].ycor()
            self.turtle[t_num].goto(new_x, new_y)
    
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