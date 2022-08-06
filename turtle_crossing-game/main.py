import time
from turtle import Screen
from day23_turtle_crossing.player import Player
from day23_turtle_crossing.car_manager import CarManager
from day23_turtle_crossing.scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.up, 'Up')
screen.onkeypress(player.down, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_cars()
    cars.move()

    # detecta colisão do carro com o jogador. Como são vários carros, é necessário usar o loop for
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish_line():
        score.increase_score()
        player.go_to_start()
        cars.level_up()


screen.exitonclick()
