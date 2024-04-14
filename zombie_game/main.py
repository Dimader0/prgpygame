from objects import*

pg.init()

pg.draw.rect(win, background, UI) #Малювання нижнього прямокутника для інтерфейсу
win.blit(background_image, (0, 0)) # Малювання фону

bt_text = ui_font.render("Start", True, (100, 255, 255)) 

finish = True #Гра не почата одразу
pause = False #Прапорець паузи

level = 1

boss_round = False

scores = 0

player = Player(player_image, 350, 250, 50, 50, 5)

def callback():
    #Зміна всіх значень за замовчуваням
    global finish, player, scores, zombies, boss_round

    pg.mixer.music.play()

    player = Player(player_image, 350, 250, 50, 50, 5)

    scores = 0
    
    finish = False
    boss_round = False
    zombies.empty()

    for i in range(10):
        zombie = Enemy(random.choice(zombie_images), 100, 100, 50, 50, 1)
        zombie.spawn()
        zombies.add(zombie)

bt = Button(win_width/2, 100, 100, 50, (50, 50, 100), bt_text, callback=callback)

play = True

while play:
    #Основний цикл
    for e in pg.event.get():
        if e.type == pg.QUIT:
            play = False
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_p:
                pause = not pause
                if pause:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()

    if finish:
        bt.update()
        bt.draw()

    elif not pause:
        win.blit(background_image, (0, 0))

        for zombie in zombies:
            dx = zombie.rect.centerx - player.rect.centerx
            dy = zombie.rect.centery - player.rect.centery
            ang = -math.atan2(-dy, dx) - math.pi

            zombie.update(ang)
            zombie.draw()

            if player.hit_box.colliderect(zombie.hit_box):
                damage_sound.play()
                if zombie.max_hp == 15:
                    zombie.kill()
                    player.hp -= 20
                    boss_round = False
                else:
                    zombie.spawn()
                    player.hp -= 10

        for b in bullets:
            if math.sqrt((b.rect.x - player.rect.x)**2 + (b.rect.y - player.rect.y)**2) > 1000:
                b.kill()
                break    
        #Робимо перевірку колізії куль та ворогів
        collide = pg.sprite.groupcollide(bullets, zombies, True, False)

        if collide:
            enemy = list(collide.values())[0][0]#Дістає ворога до якого доторкнулася куля
            enemy.hp -= 1
            if enemy.hp == 0:
                if enemy.max_hp == 15:
                    coins_sound.play()
                    enemy.kill()
                    boss_round = False
                    scores += 10
                else: #Звичайний ворог
                    coin_sound.play()
                    enemy.spawn()
                    scores += 1

        if scores % 15 == 0 and scores != 0 and not boss_round:
            boss = Enemy(random.choice(zombie_images), - 100, -200, 120, 120, 2)
            boss.max_hp = 15
            boss.spawn()
            zombies.add(boss)
            boss_round = True
        elif scores % 30 == 0 and scores != 0:
            scores += 1
            level += 1
            for zombie in zombies:
                if zombie.max_hp != 15:
                    zombie.max_hp += 1
                if level >= 6:
                    zombie.speed += 1

        player.draw()
        player.update()
        
        bullets.draw(win)
        bullets.update()

        pg.draw.rect(win, background, UI) #Малювання прямокутного інтерфейсу

        score_text = ui_font.render(f"Coins: {scores}", True, (150, 200, 50))
        win.blit(score_text, (win_width - 180, win_height - 45))

        health_text = ui_font.render(f"HP: {player.hp}", True, (255, 50, 50))
        win.blit(health_text, (0, win_height - 45))  

        if player.hp <= 0:
            finish = True
            pg.draw.rect(win, background, UI)
            lose_text = ui_font.render("You died...", True, (255, 50, 50))
            win.blit(lose_text, (250, win_height - 45))
            pg.mixer.music.stop()
            zombies.empty()
        else:
            level_text = ui_font.render(f"Level: {level}", True, (200, 200, 200))
            win.blit(level_text, (280, win_height - 45))

    else:
        pg.draw.rect(win, background, UI)
        pause_text = ui_font.render("Pause", True, (200, 200, 200))
        win.blit(pause_text, (290, win_height - 45))

   
    pg.display.update()
    clock.tick(FPS)