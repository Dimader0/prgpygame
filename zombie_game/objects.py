import random
import math

from pygame.sprite import _Group 
from settings import *

init()

class GameSprite(sprite.Sprite):
    #Основний клас спадкоємець від Sprite. Від цього класу створена Куля, Ворог, Гравець

    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        #Базові властивості та зоображення
        self.w = w
        self.h = h
        self.speed = speed
        self.image = transform.scale(image.load(img).convert_alpha(), (w, h))
        self.start_image = self.image #Стартове зоображення від якого виконується поворот
        
        #Створення підпису. За замовчуванням вимкнутий
        self.font = font.Font(None, 30)
        self.text = ""
        self.label = self.font.render(self.text, True, (100, 50 , 50))
        self.text_visible = False

        #Отримання прямокутника від зоображення
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        #Створення хіт-бокс. Прямокутник в два рази менший за стартовий
        self.hit_box = Rect(self.rect.x, self.rect.y, w/2, h/2)
        