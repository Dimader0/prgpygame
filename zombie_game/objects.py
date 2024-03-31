import random
import math

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

    def change_image(self, new_image):
        #Змінна зоображення на нове
        self.image = transform.scale(image.load(new_image).convert_alpha(), (self.w, self.h))
        self.start_image = self.image

    def rotate(self, angle):
        #Поворот спрайта
        self.image = transform.rotate(self.start_image, angle)
        self.rect = self.image.get_rect(center = (self.rect.centerx, self.rect.centery))
    
    def draw(self):
        #Відмалювання спрайта та підпису
        win.blit(self.image, self.rect)
        if self.text_visible:
            rect = self.label.get_rect()
            win.blit(self.label, (self.rect.centerx - rect.width /2, self.rect.centery + 50))

class Player(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.reload = 0 #затримка між пострілами
        self.rate = 0 #скорострільність
        self.max_hp = 100
        self.hp = 100
        self.text = f"Здоров'я: {self.hp}/{self.max_hp}"

    def update(self):
        #Переміщення, поворот та постріл
        self.hit_box.center = self.rect.center
        self.label = self.font.render(f"Здоров'я: {self.hp}/{self.max_hp}", True, (100, 50 ,50))
        
        keys = key.get_pressed()
        but = mouse.get_pressed()

        #Переміщення
        if keys[K_a] and self.rect.x > 0:
            self.rect.centerx -= self.speed
        if keys[K_d] and self.rect.x < win_width - self.rect.width:
            self.rect.centerx += self.speed
        if keys[K_w] and self.rect.y > 0:
            self.rect.centery -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.centery += self.speed
        
        #Постріл та затримка між ними
        
        

        #Поворот
        pos = mouse.get_pos()
        dx = pos[0] - self.rect.centerx
        dy = self.rect.centery - pos[1]

        ang = math.degrees(math.atan2(dy, dx))

        self.rotate(ang-90)
            