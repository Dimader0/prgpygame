from classes import *

player = Player(player_image, 40, 250, 60, 80, 5)

enemy_list = pg.sprite.Group()
enemy_list.empty()

enemy = Enemy(enemy_image, 0, random.randint(50, win_higth - 50), 150, 140, 2)

w1 = Wall(59, 214, 219, 100, 20, 450, 10)
w2 = Wall(59, 214, 219, 100, 480, 350, 10)
w3 = Wall(59, 214, 219, 100, 20, 10, 340)
w4 = Wall(59, 214, 219, 200, 130, 10, 350)
w5 = Wall(59, 214, 219, 300, 30, 10, 360)
w6 = Wall(59, 214, 219, 400, 130, 10, 350)

walls = [w1, w2, w3, w4, w5, w6]


while play:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            play = False

    win.blit(background_image, (0,0))
    player.draw()
    player.update()

    enemy.draw()
    enemy.update()
    
    for i in walls:
        i.draw()

    pg.display.update()
    clock.tick(FPS)