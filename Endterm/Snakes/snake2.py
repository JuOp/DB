import pygame, sys
import random, time
import json
from pygame.locals import *


pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((830, 630))
redline = pygame.Surface((810, 610))
Zone = pygame.Surface((800, 600))
pygame.display.set_caption("Snake")

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)


def to_list(st):
    e = len(st)
    y = []
    z = []
    sk = -1
    for i in range(0, e):
        if i > sk:
            if st[i] >= '0' and st[i] <= '9':
                x1 = 0
                for j in range(i, e):
                    if st[j] >= '0' and st[j] <= '9':
                        x1 = x1 * 10 + int(st[j])
                    else:
                        sk = j
                        break
                y.append(x1)

    f = len(y)
    for i in range(0, f - 1, 2):
        z.append([y[i], y[i + 1]])
    return z

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(40, 800-40)
        self.y = random.randint(40, 600-40)

    def gen(self):
        self.x = random.randint(40, 800-40)
        self.y = random.randint(40, 600-40)

    def draw(self):
        pygame.draw.rect(screen, BLUE, (self.x, self.y, 10, 10))


class Snake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.size = 1
        self.elements = [[x, y]]
        self.radius = 10
        if x < 400:
            self.dx = 5 # right
            self.dy = 0
        else:
            self.dx = -5 # left
            self.dy = 0
        self.is_add = False
        self.bull = False
        self.speed = 10



    def draw(self, clr):
        for element in self.elements:
            pygame.draw.circle(screen, clr, element, self.radius)

    def add_to_snake(self):
        self.size += 1
        self.elements.append([0, 0])
        self.is_add = False
        if self.size % 3 == 0:
            self.speed += 10

    def move(self):
        if self.is_add:
            self.add_to_snake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

        if lvl1 == False:
            if self.elements[0][0] < 15:
                self.elements[0][0] = 800
            if self.elements[0][0] > 800:
                self.elements[0][0] = 15
            if self.elements[0][1] < 15:
                self.elements[0][1] = 600
            if self.elements[0][1] > 600:
                self.elements[0][1] = 15
        else:
            if self.elements[0][0] < 15:
                self.bull = True
            if self.elements[0][0] > 800:
                self.bull = True
            if self.elements[0][1] < 15:
                self.bull = True
            if self.elements[0][1] > 600:
                self.bull = True


    def eat(self, foodx, foody):
        x = self.elements[0][0]
        y = self.elements[0][1]

        if foodx - 3 <= x <= foodx + 13 and foody - 3 <= y <= foody + 13:
            return True
        return False



snake1 = Snake(100, 100)
snake2 = Snake(700, 100)
food = Food()

FOOD = pygame.sprite.Group()
FOOD.add(food)

running = True

d = 5
FPS = 60
clock = pygame.time.Clock()

lvl1 = False

while running:
    if snake1.speed>=snake2.speed:
        x=snake1.speed
    else:
        x=snake2.speed
    clock.tick(x)
    #Border_is_touched
    if snake1.bull or snake2.bull:
        running = False
    #colidony of snakes
    if (snake1.elements[0] in snake2.elements[:]) or (snake2.elements[0] in snake1.elements[:]):
        running = False
    #LVL
    if x >= 30:
        lvl1 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #save the game
            y = str("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10}")
            z = open("saved_game.txt", "w")
            z.write(y.format(x, snake1.elements, snake2.elements, snake1.size, snake2.size, food.x, food.y, snake1.dx, snake1.dy, snake2.dx, snake2.dy))
            z.close()
            running = False
        if event.type == pygame.KEYDOWN:
            #continue saved game
            if event.key == pygame.K_z:
                z = open("saved_game.txt", "r")
                saved_data = z.readline()
                arr = saved_data.split(sep=';')
                z.close()
                snake1.speed = int(arr[0])
                snake1.elements = to_list(arr[1])
                snake2.elements = to_list(arr[2])
                snake1.size = int(arr[3])
                snake2.size = int(arr[4])
                food.x = int(arr[5])
                food.y = int(arr[6])
                snake1.dx = int(arr[7])
                snake1.dy = int(arr[8])
                snake2.dx = int(arr[9])
                snake2.dy = int(arr[10])

            if event.key == pygame.K_ESCAPE:
                # save the game
                y = str("{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10}")
                z = open("saved_game.txt", "w")
                z.write(y.format(x, snake1.elements, snake2.elements, snake1.size, snake2.size, food.x, food.y, snake1.dx, snake1.dy, snake2.dx, snake2.dy))
                z.close()
                running = False
            if event.key == pygame.K_RIGHT and snake1.dx != -d:
                snake1.dx = d
                snake1.dy = 0
            if event.key == pygame.K_LEFT and snake1.dx != d:
                snake1.dx = -d
                snake1.dy = 0
            if event.key == pygame.K_UP and snake1.dy != d:
                snake1.dx = 0
                snake1.dy = -d
            if event.key == pygame.K_DOWN and snake1.dy != -d:
                snake1.dx = 0
                snake1.dy = d

            if event.key == pygame.K_d and snake2.dx != -d:
                snake2.dx = d
                snake2.dy = 0
            if event.key == pygame.K_a and snake2.dx != d:
                snake2.dx = -d
                snake2.dy = 0
            if event.key == pygame.K_w and snake2.dy != d:
                snake2.dx = 0
                snake2.dy = -d
            if event.key == pygame.K_s and snake2.dy != -d:
                snake2.dx = 0
                snake2.dy = d

            if event.key == pygame.K_1:
                snake1.is_add = True
            if event.key == pygame.K_2:
                snake2.is_add = True

    
    if snake1.eat(food.x, food.y):
        snake1.is_add = True
        food.kill()
        food.gen()

    if snake2.eat(food.x, food.y):
        snake2.is_add = True
        food.kill()
        food.gen()

    Zone.fill(BLACK)
    redline.fill(RED)
    screen.fill(WHITE)
    if lvl1:
        screen.blit(redline, [10, 10])
    screen.blit(Zone, [15, 15])
    snake1.move()
    snake2.move()
    snake1.draw(RED)
    snake2.draw(GREEN)
    food.draw()
    pygame.display.flip()

pygame.quit()