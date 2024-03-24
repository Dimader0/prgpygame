from pygame import *

init()

#Характеристики вікна
win_width = 700
win_height = 500
FPS = 60

#Створення вікна
win = display.set_mode((win_width, win_height))
clock = time.Clock()

#Зоображення
player_image = './textures/player.png'
zombie_images = ['./textures/zombie1.png', './textures/zombie2.png', './textures/zombie3.png']
