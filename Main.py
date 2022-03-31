import pygame
from sys import exit
from Settings import *
from Cowboy import Cowboy
from Player import Player
from Level import Level
from Pets import FireSpirit
from Slayer import Slayer
from Portal import Portal
from random import randint
pygame.init()

FPS = 27
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quatt Fighters")
clock = pygame.time.Clock()

SKY = pygame.transform.scale(pygame.image.load("Background/background.png"),(WIDTH,HEIGHT)).convert_alpha()
Mount = pygame.transform.scale(pygame.image.load("Background/bg_2.png"),(WIDTH,HEIGHT)).convert_alpha()

data = None
with open ("Layouts/lvl0.txt", "r") as myfile: data = myfile.read().splitlines()
for i in range(len(data)):
  data[i] = data[i].replace("\t"," ")
  data[i] = data[i].split(" ")
  for j in range(len(data[i])):
    if data[i][j] == '':
      data[i].pop(j)
      break

level = Level(data)
p1 = Cowboy(500, 500, 32, 50, 10, 25, 25, 0.5)
pets = [FireSpirit(300, 400, 32, 32, 8, 25, 25, 5, "Fire Spirit", { "Idle": 6, "Move": 8 })]
entityList = [
  Slayer(randint(1000,2000), 500, 75, 100, 1, 25, 25, 0.5),
]

portal = Portal(800, 450, -1)

def draw():
  portal.open_portal(screen)
  level.draw_map(screen, p1, entityList, pets)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
  screen.fill("black")

  screen.blit(SKY,(0,0))
  screen.blit(Mount,(0,0))

  draw()
  pygame.display.update()
  clock.tick(FPS)