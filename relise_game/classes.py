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
        
    direction = "right"

    def spawn(self):
        self.rect.x = 0
        self.rect.y = random.randint(0, win_higth)
    
    def update(self):
        self.direction = "right"    
        self.rect.x += self.speed
        if self.rect.x > 700 or self.rect.x < 0:
            self.spawn()

class Wall(pg.sprite.Sprite):
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        
        self.image = pg.Surface((wall_width, wall_height))

        self.image.fill((color1, color2, color3))

        self.rect = self.image.get_rect()

        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
            