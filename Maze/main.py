from pygame import *
from time import sleep

init()

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
            self.rect.y -= 5
        if keys[K_s] and self.rect.y < 390:
            self.rect.y += 5
        if keys[K_d] and self.rect.x < 610:
            self.rect.x += 5
        if keys[K_a] and self.rect.x > 10:
            self.rect.x -= 5
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y


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
    def __init__(self, color1, color2, color3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        
        self.image = Surface((wall_width, wall_height))

        self.image.fill((color1, color2, color3))

        self.rect = self.image.get_rect()

        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))


screen = display.set_mode((700, 500))
display.set_caption("Лабіринт")
bg = transform.scale(image.load("bg.jpg"), (700, 500))
player = Player("player.png", 10, 390, 60, 80)
enemy = Enemy("enemy.png", 600, 200, 80, 100)

goal = GameSprite("treasure.png", 550, 400, 80, 60)
goal2 = GameSprite("treasure.png", 600, 20, 80, 60)
goal3 = GameSprite("treasure.png", 15, 40, 80, 60)
goal4 = GameSprite("treasure.png", 220, 250, 80, 60)

w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 20, 10, 340)
w4 = Wall(154, 205, 50, 200, 130, 10, 350)
w5 = Wall(154, 205, 50, 300, 30, 10, 360)
w6 = Wall(154, 205, 50, 400, 130, 10, 350)

walls = [w1, w2, w3, w4, w5, w6]

game = True
clock = time.Clock()
FPS = 60

mixer.init()
#mixer.music.load("")
#mixer.music.play()

goals_col_d = 0
goals_colect = 0
hp = 3

font.init()
font = font.Font(None, 70)
win = font.render("You win!", True, (235, 215, 0))
lose = font.render("You lose!", True, (180, 0, 10))

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    screen.blit(bg, (0, 0))
    player.draw()
    enemy.draw()
    if goals_col_d != 1 or not goals_col_d < 1:
        goal.draw()
    if goals_col_d != 2 or not goals_col_d < 2:
        goal2.draw()
    if goals_col_d != 3 or not goals_col_d < 3:
        goal3.draw()
    if goals_col_d != 4 or not goals_col_d < 4:
        goal4.draw()
    for w in walls:
        w.draw()

    for w in walls:
        if sprite.collide_rect(player, w):
            player.set_pos(10, 390)

    player.moving()
    enemy.moving()

    if sprite.collide_rect(player, enemy):
        hp -= 1
        player.set_pos(10, 390)
        if hp == 0:
            screen.blit(lose, (200, 200))
            display.update()
            sleep(2)
            game = False

    if sprite.collide_rect(player, goal):
        goals_col_d += 1
        goals_colect += 1
        display.update()
    if sprite.collide_rect(player, goal2):
        goals_col_d += 1
        goals_colect += 1
        display.update()
    if sprite.collide_rect(player, goal3):
        goals_col_d += 1
        goals_colect += 1
        display.update()
    if sprite.collide_rect(player, goal4):
        goals_col_d += 1
        goals_colect += 1
        display.update()
        

    if goals_colect == 4:
        screen.blit(win, (200, 200))
        display.update()
        sleep(2)
        game = False

    display.update()
    clock.tick(FPS)
