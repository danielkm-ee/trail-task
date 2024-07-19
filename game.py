# Simulation environment for Neural networks performing foraging tasks
# Author(s) : Daniel Monahan
# contact(s) : danielkm@github.com
#
# 


# WIP Currently porting controls, object classes, and trail functionality from trail-game
import pygame
import time

GRID_SIZE = 32

# window size
SCALE = 20
WIDTH = GRID_SIZE * SCALE
HEIGHT = GRID_SIZE * SCALE

# colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
gray = pygame.Color(100, 100, 100)
red = pygame.Color(125, 10, 10)
lightyellow = pygame.Color(250, 245, 170)

agent = pygame.image.load('agent.png')
agent = pygame.transform.scale(agent, (WIDTH//GRID_SIZE, HEIGHT//GRID_SIZE))
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 22)
txt = font.render('⮝', True, white)

class Ant:
    def __init__(self, position=[0, 0]):
        self.position = position
        self.dir = 0 # 0 = right, 1 = up, 2 = left, 3 = down

    def move(self):
        if (self.dir == 0):
            self.position[0] += WIDTH // GRID_SIZE
        elif (self.dir == 1):
            self.position[1] -= HEIGHT // GRID_SIZE
        elif (self.dir == 2):
            self.position[0] -= WIDTH // GRID_SIZE
        elif (self.dir == 3):
            self.position[1] += HEIGHT // GRID_SIZE
        else :
            raise ValueError
            print("Ant.dir is out of range!")


    def draw(self):
        sprite = pygame.transform.rotate(agent, self.dir * (360/4))
        map_.surface.blit(sprite, (self.position[0], self.position[1]) )


class Map:
    def __init__(self, width=WIDTH, height=HEIGHT, color=lightyellow):
        self.width = width
        self.height = height
        self.color = color

        self.surface = pygame.display.set_mode((self.width, self.height))

    def draw(self):
        self.surface.fill(self.color)
        
        for x in range(0, self.width, self.width // GRID_SIZE):
            for y in range(0, self.height, self.height // GRID_SIZE):
                pygame.draw.line(self.surface, gray, (x, 0), (x, self.height), 2)
                pygame.draw.line(self.surface, gray, (0, y), (self.width, y), 2)

class Pellet:
    def __init__(self, position=[WIDTH/GRID_SIZE * 10, HEIGHT/GRID_SIZE * 10]):
        self.position = position
        self.wasEaten = False

    def draw(self):
        pygame.draw.rect(map_.surface, red, pygame.Rect(self.position[0], self.position[1], WIDTH / GRID_SIZE, HEIGHT / GRID_SIZE))

class Trail:
    def __init__(self):
        self.pellets = list()
    
    def addPellet(position):
       return


# Initialising pygame
pygame.init()

# FPS (frames per second) controller
fps = 120


def rlm_controls(ant, key):
    if (key == pygame.K_j):
        ant.dir = (ant.dir + 1) % 4
    elif (key == pygame.K_k):
        ant.dir = (ant.dir - 1) % 4
    elif (key == pygame.K_f):
        ant.move()
    return

font = pygame.font.Font
ant = Ant();
map_ = Map();
pellet = Pellet();

while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            rlm_controls(ant, event.key)
            if event.key == pygame.K_q:
                pygame.quit()
                quit()

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    
    map_.draw()
    pellet.draw()
    ant.draw()

  

    pygame.display.update()

