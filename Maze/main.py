from pygame import *
import pygame

class GameSprite(sprite.Sprite):
    def __init__ (self, img, x, y, w, h):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def moving(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 10:
            self.rect.y -= 10
        if keys[K_s] and self.rect.y < 390:
            self.rect.y += 10
        if keys[K_d] and self.rect.x < 610:
            self.rect.x += 10
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= 10

class Enemy(GameSprite):
    direction = "left"
    def moving(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 680:
            self.direction = "left"

        if self.direction == "right":
            self.rect.x += 5
        else:
            self.rect.x -= 5

class Wall(sprite.Sprite):
    pass

screen = display.set_mode((700, 500))
display.set_caption("Лабіринт")
bg = transform.scale(image.load("bg.jpg"), (700, 500))
player = Player("player.png", 110, 390, 80, 100)
enemy = Enemy("enemy.png", 600, 200, 80, 100)

game = True
clock = time.Clock()
FPS = 60

mixer.init()
#mixer.music.load("")
#mixer.music.play()


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    screen.blit(bg, (0, 0))
    player.draw()
    enemy.draw()

    player.moving()
    enemy.moving()

    if pygame.sprite.collide_rect(player, enemy):
        print("1")


    display.update()
    clock.tick(FPS)
