from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 14, 'normal')


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', 'r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.print_score()

    def print_score(self):
        """Prints the current score"""
        self.clear()
        self.write(f'Score: {self.score} \tHigh Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by 1, everytime snake eats food"""
        self.score += 1
        self.print_score()

    def game_over(self):
        """Prints game over"""
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.print_score()
