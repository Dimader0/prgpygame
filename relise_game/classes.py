import random
from settings import *


class GameSprite(pg.sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        self.image = pg.transform.scale(pg.image.load(img), (w,h))

        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.hitbox = pg.Rect(self.rect.x, self.rect.y, w/2, h/2)

    def draw(self):
        win.blit(self.image, self.rect)

class Player(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.hp = 100

    def update(self):
        keys = pg.key.get_pressed()
        but = pg.mouse.get_pressed()

        if keys[pg.K_a] and self.rect.x > 0:
            self.rect.centerx -= self.speed
        if keys[pg.K_d] and self.rect.x < win_width - self.rect.width:
            self.rect.centerx += self.speed
        if keys[pg.K_w] and self.rect.y > 0:
            self.rect.centery -= self.speed
        if keys[pg.K_s] and self.rect.y < win_higth - self.rect.height:
            self.rect.centery += self.speed

class Enemy(GameSprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__(img, x, y, w, h, speed)
        self.hp = 1

    def spawn(self):
        self.rect.x = win_width + 100
        self.rect.y = random.randint(0, win_higth)
    
    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0:
            self.spawn()
            