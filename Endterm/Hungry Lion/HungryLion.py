import pygame
import random
import time
import sys

pygame.init()
WIDTH = 1000
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Blue(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 100
        self.y = 600
        self.dx = 0
        self.dy = 0

    def move(self):
        if self.x >= WIDTH - 20 and self.dx > 0:
            self.dx = 0
        if self.x <= 0 and self.dx < 0:
            self.dx = 0

        if self.y >= HEIGHT - 20 and self.dy > 0:
            self.dy = 0
        if self.y <= 0 and self.dy < 0:
            self.dy = 0

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 20, 20))
        self.x += self.dx
        self.y += self.dy


class Green(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, 970)
        self.y = random.randint(0, 730)
        self.dx = 0
        self.dy = 0

    def move(self):
        if random.randint(0, 1) == 0 and self.x > 0:
            self.dx = -random.randint(1, 5)
        elif self.x < WIDTH - 30:
            self.dx = random.randint(1, 5)

        if random.randint(0, 1) == 0 and self.y > 0:
            self.dy = -random.randint(1, 5)
        elif self.y < HEIGHT - 30:
            self.dy = random.randint(1, 5)

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, 30, 20))
        self.x += self.dx
        self.y += self.dy


class Red(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = random.randint(0, 970)
        while True:
            self.y = random.randint(0, 730)
            if 500 >= self.y or self.y >= 700:
                break

    def move(self):
        self.y += random.randint(5, 8)
        if self.y >= HEIGHT:
            self.y = -20

    def draw(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, 30, 20))


clock = pygame.time.Clock()

player = Blue()
foods = pygame.sprite.Group()
for i in range(25):
    f = Green()
    foods.add(f)

red = pygame.sprite.Group()
for i in range(40):
    r = Red()
    red.add(r)

score = 0
eat = 25

small = pygame.font.SysFont("Calibri", 20)
big = pygame.font.SysFont("Calibri", 60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP and player.y > 10:
                player.dx = 0
                player.dy = -10
            if event.key == pygame.K_DOWN and player.y < HEIGHT - 10:
                player.dx = 0
                player.dy = 10
            if event.key == pygame.K_RIGHT and player.x < WIDTH - 10:
                player.dx = 10
                player.dy = 0
            if event.key == pygame.K_LEFT and player.x > 10:
                player.dx = -10
                player.dy = 0

    screen.fill(WHITE)
    player.move()
    player.draw()
    for i in foods:
        i.move()
        i.draw()
    for i in red:
        i.move()
        i.draw()

    for i in foods:
        if (player.x > i.x or i.x > player.x + 15) and (player.x > i.x + 25 or i.x + 25 > player.x + 15) or (
                player.y > i.y or i.y > player.y + 15) and (player.y > i.y + 15 or i.y + 15 > player.y + 15):
            continue
        i.kill()
        pygame.mixer.Sound('eda.wav').play()
        score += 1
        eat -= 1

    for i in red:
        if (player.x > i.x or i.x > player.x + 15) and (player.x > i.x + 25 or i.x + 25 > player.x + 15) or (
                player.y > i.y or i.y > player.y + 15) and (player.y > i.y + 15 or i.y + 15 > player.y + 15):
            continue
        i.y = -20
        pygame.mixer.Sound('vrag.wav').play()
        score -= 1

    screen.blit(small.render("SCORE:" + str(score), True, BLACK), (10, 10))
    if score < 0:
        pygame.mixer.Sound('lost.wav').play()
        screen.fill(RED)
        screen.blit(big.render("Game Over", True, WHITE), (300, 300))
        pygame.display.update()
        time.sleep(3)
        break

    if eat <= 0:
        pygame.mixer.Sound('win.wav').play()
        screen.fill(GREEN)
        screen.blit(big.render("Game Over", True, WHITE), (300, 300))
        pygame.display.update()
        time.sleep(3)
        break

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
