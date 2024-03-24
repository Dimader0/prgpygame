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
bullet_image = './textures/bullet.png'

#Фонове зоображення
background_image = transform.scale(image.load('./textures/background.png'), (win_width, win_height))

#Звуки
fire_sound = mixer.Sound('./sounds/fire.ogg')
coin_sound = mixer.Sound('./sounds/coin.ogg')
coins_sound = mixer.Sound('./sounds/coins.ogg')
damage_sound = mixer.Sound('./sounds/damage.ogg')
death_sound = mixer.Sound('./sounds/death.ogg')

#Музика
mixer.music.load('./sounds/music.mp3')

#Колір фону інтерфейса
background = (150, 150, 100)

#Групи для куль та ворогів
bullets = sprite.Group()
zombies = sprite.Group()

#Шрифт інтерфейса
ui_font = font.Font(None, 50)

#Інтерфейс
UI = Rect(0, win_height, win_width, 50)

