from pygame import *

width = 700
height = 500
win = display.set_mode((width, height))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (width, height))
game = True
finish = False
fps = 60
clock = time.Clock()

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')

font.init()
font = font.Font(None, 70)
winer = font.render('u win🆘🍌🍌🤳🎉🎉🌹🌹🐱‍👓', True, (252, 15, 192))
loser = font.render('u lose🤦‍♀️🥺🥺😋😔🐛🐛🥕🥕🦐', True, (231, 254, 82))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 5:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < width - 5:
            self.rect.x += self.speed
class Enemy(GameSprite):
    direction = "left"
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= width - 85:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, width, height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        win.blit(self.image, (self.rect.x, self.rect.y))
player = Player('hero.png', 5, height - 80, 4)
enemy = Enemy('cyborg.png', width - 80, 280, 2)
final = GameSprite('treasure.png', width - 120, height - 80, 0)
wall_1 = Wall(44, 255, 0, 100, 20, 450, 10)
wall_2 = Wall(44, 255, 0, 100, 480, 350, 10)
wall_3 = Wall(44, 255, 0, 100, 20, 10, 380)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        win.blit(background, (0, 0))
        player.update()
        player.reset()
        enemy.update()
        enemy.reset()
        final.reset()
        wall_1.draw_wall()
        wall_2.draw_wall()
        wall_3.draw_wall()
        if sprite.collide_rect(player, final):
            finish = True
            money.play()
            win.blit(winer, (200, 200))
        if sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall_1) or sprite.collide_rect(player, wall_2) or sprite.collide_rect(player, wall_3):
            finish = True
            win.blit(loser, (200, 200))
            kick.play()
    display.update()
    clock.tick(fps)