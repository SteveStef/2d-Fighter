import pygame
from Images import getAnimation
from random import randint

class Projectile:
  def __init__(self, x, y, vel, facing):
    self.images = getAnimation("Effects/Bullet/firebullet1", 4, 2.5)
    self.impactImgs = getAnimation("Effects/Bullet/fireimpact", 2, 2)
    self.rect = pygame.Rect(x, y, 20, 10)
    self.changeY = randint(-1,1)
    self.direction = pygame.math.Vector2(0, 0)
    self.direction.x = facing
    self.vel = vel
    self.frame = 0
    self.frameRate = 0.4
    self.framei = 0
    self.impacting = False
    self.dead = False


  def animate(self, screen):
    if self.frame >= len(self.images): self.frame = 0
    img = self.images[int(self.frame)]
    offX, offY = 10, 0
    if self.direction.x == -1:
      img = pygame.transform.flip(img,True,False)
      offX = -30
    screen.blit(img, (self.rect.x + offX, self.rect.y-10))
    self.frame += self.frameRate


  def drawHitbox(self, screen):
    pygame.draw.rect(screen, "red", self.rect, 1)


  def move(self):
    self.rect.x += self.vel * self.direction.x
    self.rect.y += self.changeY
  

  def impact(self, screen):
    if self.framei >= len(self.impactImgs): self.dead = True
    if self.dead: return
    img = self.impactImgs[int(self.framei)]
    screen.blit(img, (self.rect.x + 10*self.direction.x, self.rect.y-10))
    self.framei += 0.6


  def update(self, screen):
    if self.impacting: self.impact(screen)
    else:
      self.animate(screen)
      self.move()


class Slash:
  def __init__(self,x,y):
    self.images = getAnimation("Effects/Spark/Hit", 4, 2)
    self.frame = 0
    self.frameRate = 0.6
    self.active = False
    self.x = x
    self.y = y
  
  def updatePos(self,x,y):
    self.x=x
    self.y=y
    self.frame = 0

  def animate(self, screen):
    if self.frame >= len(self.images): self.active = False
    if not self.active: return
    img = self.images[int(self.frame)]
    screen.blit(img, (self.x, self.y))
    self.frame += self.frameRate