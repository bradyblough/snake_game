from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = "Courier", 24, "normal"


# scoreboard class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read()) # saves high score to txt file.
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    # scoreboard methods
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    # displays game over when user collides with wall or tail
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
    # increases the score and updates scoreboard
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
