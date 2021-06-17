from turtle import Turtle

SCORE = 0
ALIGNMENT = 'center'
FONT = ('Arial', 14, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.print_score()

    def print_score(self):
        """Prints the current score"""
        self.write(f'Score: {SCORE}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1, everytime snake eats food"""
        global SCORE
        self.clear()
        SCORE += 1
        self.print_score()

    def game_over(self):
        """Prints game over"""
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
