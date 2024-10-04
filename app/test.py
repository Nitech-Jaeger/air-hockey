from game.AirHockey import AirHockey

WIDTH = 1000
HEIGHT = 500
GOAL_SIZE = 100
GOAL_POSITION = 200
FINISH_POINT = 5

game  = AirHockey(0,0,WIDTH,HEIGHT,GOAL_POSITION,GOAL_SIZE,FINISH_POINT)
game.start_game()

li = game.get_entity_list()
for el in li:
    print(el)

FRAME = 60
for i in range(FRAME):
    game.process_hit_and_move()
    li = game.get_entity_list()
    for el in li:
        print(el)