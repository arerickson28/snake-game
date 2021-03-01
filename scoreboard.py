from turtle import Turtle

class Scoreboard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup
        self.goto(0, 265)
        self.score = 0
        self.color("blue")
        self.write(f"Score: {self.score}", move = False, align = "center", font = ("Papyrus", 20, "normal"))
        
        
        

    def update_score(self) :
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", move = False, align = "center", font = ("Papyrus", 20, "normal"))
    