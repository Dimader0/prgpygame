from objects import*

init()

draw.rect(win, background, UI) #Малювання нижнього прямокутника для інтерфейсу
win.blit(background_image, (0, 0)) # Малювання фону

bt_text = ui_font.render("Start", True, (100, 255, 255)) 

finish = True #Гра не почата одразу
pause = False #Прапорець паузи

level = 1

mixer.init()
mixer.music.load("./sounds/music.mp3")
mixer.music.play()

while True:
    #Основний цикл
    for e in event.get():
        if e.type == QUIT:
            exit()

    display.update()
    clock.tick(FPS)