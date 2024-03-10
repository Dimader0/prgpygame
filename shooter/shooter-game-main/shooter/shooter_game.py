#Створи власний Шутер!

from pygame import *
from time import sleep

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
    def move(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= 10
        if keys[K_d] and self.rect.x < 615:
            self.rect.x += 10
    
    def fire(self):
        pass



screen = display.set_mode((700, 500))
display.set_caption("shooter")
bg = transform.scale(image.load("galaxy.jpg"), (700, 500))
ship = Player("rocket.png", 250, 390, 70, 100)

mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

font.init()
font = font.Font(None, 40)
score_font = font.render("Рахунок:", True, (255, 255, 255))
lose_font = font.render("Пропущено:", True, (255, 255, 255))
score = font.render("0", True, (255, 255, 255))
lose = font.render("0", True, (255, 255, 255))


clock = time.Clock()
FPS = 60

play = True

while play:
    for e in event.get():
        if e.type == QUIT:
            play = False

    screen.blit(bg, (0, 0))
    screen.blit(score_font, (0, 0))
    screen.blit(lose_font, (0, 30))
    screen.blit(score, (125, 2))
    screen.blit(lose, (175, 32))
    ship.draw()
    ship.move()

    display.update()
    clock.tick(FPS)