from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.speed('fastest')
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align=ALIGNMENT, font=FONT)




























        