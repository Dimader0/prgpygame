#Створи власний Шутер!

from typing import Any
from pygame import *
from time import sleep
from random import randint

score = 0
lost = 0

class GameSprite(sprite.Sprite):
    def __init__ (self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < 615:
            self.rect.x += self.speed
    
    def fire(self):
        bullet = Bullet("./shooter/shooter-game-main/shooter/bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

    def fire_3(self):
        bullet = Bullet("./shooter/shooter-game-main/shooter/bullet.png", self.rect.centerx, self.rect.top, 15, 20, -15)
        bullet2 = Bullet("./shooter/shooter-game-main/shooter/bullet.png", self.rect.centerx + 15, self.rect.top, 15, 20, -15)
        bullet3 = Bullet("./shooter/shooter-game-main/shooter/bullet.png", self.rect.centerx - 15, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
        bullets.add(bullet2)
        bullets.add(bullet3)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            lost +=1
            self.rect.y = -20
            self.rect.x = randint(0, 620)
    
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()


screen = display.set_mode((700, 500))
display.set_caption("shooter")
bg = transform.scale(image.load("./shooter/shooter-game-main/shooter/galaxy.jpg"), (700, 500))
ship = Player("./shooter/shooter-game-main/shooter/rocket.png", 250, 390, 70, 100, 10)

bullets = sprite.Group()
enemies = sprite.Group()

for i in range(6):
    enemy = Enemy("./shooter/shooter-game-main/shooter/ufo.png", randint(0, 620), -20, 80, 50, randint(1, 3))
    enemies.add(enemy)


mixer.init()
mixer.music.load("./shooter/shooter-game-main/shooter/space.ogg")
mixer.music.play()
fire_sound = mixer.Sound("./shooter/shooter-game-main/shooter/space.ogg")

font.init()
font = font.Font(None, 40)
win = font.render("You win!", True, (235, 215, 0))
lose = font.render("You lose!", True, (180, 0, 10))

clock = time.Clock()
FPS = 60

play = True

def add_new_eneny(e):
    for i in range(e):
        enemy = Enemy("./shooter/shooter-game-main/shooter/ufo.png", randint(0, 620), -20, 80, 50, randint(1, 3))
        enemies.add(enemy)

while play:
    for e in event.get():
        if e.type == QUIT:
            play = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire_3()
                fire_sound.play()
        elif e.type == MOUSEBUTTONDOWN:
            ship.fire()
            fire_sound.play()
            
    screen.blit(bg, (0, 0))

    score_font = font.render("Рахунок: " + str(score), True, (255, 255, 255))
    lost_font = font.render("Пропущено: "+ str(lost), True, (255, 255, 255))

    screen.blit(score_font, (0, 0))
    screen.blit(lost_font, (0, 30))

    ship.draw()
    ship.move()

    enemies.draw(screen)
    enemies.update()

    bullets.draw(screen)
    bullets.update()

    for bullet in bullets:
        for enemy in enemies:
            if sprite.collide_rect(bullet, enemy):
                bullet.kill()
                enemy.set_pos(randint(0, 620), -20)
                score += 1
    
    if score == 5:
        add_new_eneny(1)
    if score == 6:
        add_new_eneny(1)
    if score == 10:
        add_new_eneny(1)

    if score == 100:
        screen.blit(win, (200, 200))
        play = False
    
    if lost >= 40:
        screen.blit(lose, (200, 200))
        play = False

    display.update()
    clock.tick(FPS)