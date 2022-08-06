from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # ABAIXO o atributo para aumentar a velocidade da bola quando quicar em um paddle
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # transforma as coordenadass y no sentido oposto( de + para - e de  - transforma em +
    # faz quicar na parte de cima de de baixo da tela
    def bounce_y(self):
        self.y_move *= -1

    # faz a bola quicar com os paddles
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_game(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()


# para ele ricochetear de volta, fazemos com que as coordenadas y dele sejam invertidas, desta forma, quando a
# bola bate na parede, as coordenas y fazem com que a bola se mova em um sentido oposto, mas as coordendas x
# continuam iguais