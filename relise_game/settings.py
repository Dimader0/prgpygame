import pygame as pg 

pg.init()

win_width = 700
win_higth = 500

win = pg.display.set_mode((win_width, win_higth))

clock = pg.time.Clock()
FPS = 60
play = True
level = 1
scores = 0

player_image = "player.png"
enemy_image = "enemy.png"

background_image = pg.transform.scale(pg.image.load("bg.jpg"), (win_width, win_higth))

ui_font = pg.font.Font(None, 30)