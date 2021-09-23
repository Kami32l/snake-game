from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.pencolor("white")
        self.write("Score: 0", align=ALIGNMENT, font=FONT)

    def print_score(self):
        self.score += 1
        self.clear()
        self.goto(-60, 275)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))
        self.goto(-200, 275)
        self.write(f"Highest score: {self.highest_score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 40, "normal"))

    def print_scoreboard(self, names_scores):
        self.clear()
        self.pencolor("black")
        self.penup()
        self.goto(0, 250)
        self.write(f"Scoreboard", align="center", font=("Arial", 35, "normal"))
        y = 220
        for key in names_scores:
            self.goto(-70, y)
            self.write(f"{key}:{names_scores[key]}", align="left", font=("Arial", 25, "normal"))
            y -= 25

    def reset_score(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            # print("save score to short memory")
        self.score = 0
        self.clear()
        self.goto(-60, 275)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 15, "normal"))
        self.goto(-200, 275)
        self.write(f"Highest score: {self.highest_score}", align="center", font=("Arial", 15, "normal"))
