from Entity import Entity
import pygame
from Images import getAnimation

class Slayer(Entity):
   def __init__(self,x,y,w,h,vel,health,mana,damage):
      Entity.__init__(self,x,y,w,h,vel,health,mana,damage)
      self.status = "Idle"
      self.frame = 0
      self.frameDeath = 0
      self.jumpVel = -15
      scale = 3
      self.images = {
         "Idle": getAnimation("Characters/Slayer/Idle", 8, scale),
         "Move": getAnimation("Characters/Slayer/Move", 8, scale),
         "Attack": getAnimation("Characters/Slayer/Attack", 5, scale),
         "Hurt": getAnimation("Characters/Slayer/Hurt", 4, scale),
         "Dead": getAnimation("Characters/Slayer/Dead", 6, scale)
      }

      self.offsets = {
         "Idle": (-60, -10),
         "Move": (-60, -10),
         "Attack":(-60, -25),
         "Hurt": (-75, -10),
         "Dead": (-60, -10),
      }

      self.frameRates = {
         "Idle": 0.2,
         "Move": 0.3,
         "Attack": 0.25,
         "Hurt": 0.4,
         "Dead": 0.2
      }

   def world_shift(self, x_shift):
     self.rect.x += x_shift

   def animate(self, screen):
      if self.frame >= len(self.images[self.status]): 
        self.frame = 0
        if self.status == "Hurt": self.status = "Idle"
      img = self.images[self.status][int(self.frame)]
      if self.facing == -1: img = pygame.transform.flip(img, True, False)
      offX = self.offsets[self.status][0]
      offY = self.offsets[self.status][1]
      screen.blit(img, (self.rect.x + offX, self.rect.y + offY))
      self.frame += self.frameRates[self.status]


   def getStatus(self, player):
      if self.status == "Hurt": return
      elif abs(player.rect.x - self.rect.x) < 1000: # if in range
        if self.rect.colliderect(player.rect):
          self.status = "Attack"
          self.direction.x = 0
        else:
          self.status = "Move"
          self.getDirection(player)
      else:
        self.direction.x = 0
        self.status = "Idle"


   def getDirection(self, player):
     if player.rect.x < self.rect.x: self.direction.x = -1
     else: self.direction.x = 1


   def damage(self, dmg):
     self.health -= dmg
     if self.health <= 0: self.status = "Dead"
     if self.status == "Idle": 
        self.frame = 0
        self.status = "Hurt"


   def faceDirection(self):
     f = self.direction.x
     if f != 0: self.facing = f


   def jump(self):
    if self.hitWall and self.jCount == 0: 
      self.direction.y = self.jumpVel
      self.jCount = 1
    else:
      self.hitWall = False
      self.jCount = 0


   def deathAnimation(self, screen):
      self.status = "Dead"
      if self.frameDeath >= len(self.images[self.status]): 
        self.isDead = True
        return
      offX = self.offsets[self.status][0]
      offY = self.offsets[self.status][1]
      img = self.images[self.status][int(self.frameDeath)]
      if self.facing == -1: img = pygame.transform.flip(img, True, False)
      screen.blit(img, (self.rect.x + offX, self.rect.y + offY))
      self.frameDeath += 0.3

   def attack(self, player):
     if self.status == "Attack" and self.frame >= 3 and self.frame < 4:
       player.health -= self.dmg


   def update(self, screen, player):
    if self.health > 0:
      self.attack(player)
      self.getStatus(player)
      self.animate(screen)
      self.faceDirection()
      self.drawHealthBars(screen, 50)
      self.move()
      self.jump()
    else:
      self.deathAnimation(screen)
