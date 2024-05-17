from classes import *

player = Player(player_image, 200, 250, 50, 80, 5)

enemy_list = pg.sprite.Group()
enemy_list.empty()

enemy = Enemy(enemy_image, 100, random.randint(0, win_higth), 70, 90, 2)


while play:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            play = False

    win.blit(background_image, (0,0))
    player.draw()
    player.update()

    enemy.draw()
    enemy.update()
    

    pg.display.update()
    clock.tick(FPS)