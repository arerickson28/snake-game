from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Papyrus", 20, "normal")

class Scoreboard(Turtle) :
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.penup
        self.goto(0, 265)
        self.score = 0
        self.color("blue")
        self.write_scoreboard()
        
    
    def write_scoreboard(self) :
        self.write(f"Score: {self.score}", move = False, align = ALIGNMENT, font = FONT)

    def update_score(self) :
        self.score += 1
        self.clear()
        self.write_scoreboard()
    

    def game_over(self) :
        self.goto(0, 0)
        self.write("Game Over", align = ALIGNMENT, font = FONT)