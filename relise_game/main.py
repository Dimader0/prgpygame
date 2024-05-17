from classes import *

player = Player(player_image, 200, 250, 100, 130, 5)

enemy_list = pg.sprite.Group()
enemy_list.empty()

for i in range(5):
    enemy = Enemy(enemy_image, win_width + 100, random.randint(0, win_higth), 100, 130, 2)
    enemy.spawn()

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