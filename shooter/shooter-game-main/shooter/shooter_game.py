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


screen = display.set_mode((700, 500))
display.set_caption("shooter")
bg = transform.scale(image.load("galaxy.jpg"), (700, 500))