from objects import*

pg.init()

pg.draw.rect(win, background, UI) #Малювання нижнього прямокутника для інтерфейсу
win.blit(background_image, (0, 0)) # Малювання фону

bt_text = ui_font.render("Start", True, (100, 255, 255)) 

finish = True #Гра не почата одразу
pause = False #Прапорець паузи

level = 1

pg.mixer.music.play()

player = Player(player_image, 350, 250, 50, 50, 5)


while True:
    #Основний цикл
    for e in pg.event.get():
        if e.type == pg.QUIT:
            exit()
        if e.type == pg.KEYDOWN:
            if e.key == pg.K_p:
                pause = not pause
                if pause:
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()


    player.draw()
    player.update()
    win.blit(background_image, (0, 0))
    pg.display.update()
    clock.tick(FPS)