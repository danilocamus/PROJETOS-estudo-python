from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(position)
        self.write(f'Score: {self.score}', align='center', font=('Arial', 17, 'normal'))
        self.hideturtle()

    def r_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 17, 'normal'))

    def l_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Arial', 17, 'normal'))