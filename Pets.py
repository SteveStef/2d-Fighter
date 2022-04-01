import pygame
from Images import getAnimation
from Slayer import Slayer

class FireSpirit(Slayer):
  def __init__(self, x, y, w, h, vel, health, mana, damage, typ, frames):
    Slayer.__init__(self, x, y, w, h, vel, health, mana, damage)
    self.status = "Idle"
    self.frame = 0
    self.frameRate = 0.4
    self.vel = vel
    self.images = {
      "Idle": getAnimation(f"Characters/Pets/{typ}/Idle", frames["Idle"], 2.25),
      "Move": getAnimation(f"Characters/Pets/{typ}/Move", frames["Move"], 2.25)
    }

  def animate(self, screen, player):
    self.getStatus(player)
    if self.frame >= len(self.images[self.status]): self.frame = 0
    img = self.images[self.status][int(self.frame)]
    if self.facing == -1: img = pygame.transform.flip(img, True, False)
    screen.blit(img, (self.rect.x-20, self.rect.y-10))
    self.frame += self.frameRate

  def getStatus(self, player):
    if abs(self.rect.x - player.rect.x) < 60:
      self.status = "Idle"
      self.direction.x = 0
    else:
      self.status = "Move"
      self.getDirection(player)

  def update(self, screen, player):
    self.animate(screen, player)
    self.faceDirection()
    self.jump()

