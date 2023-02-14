from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    # Create a scoreboard to display level and number (changing)
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-200, 240)
        self.update_scoreboard()

    # Update scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
    
    # Create a function to change level number
    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
