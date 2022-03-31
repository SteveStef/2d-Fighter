import pygame
from Images import getAnimation
class Portal:
  def __init__(self, x, y, direction):
    self.x = x
    self.y = y
    self.frame = 0
    self.framRate = 0.5
    self.loops = 10
    self.openCount = 0
    self.direction = direction
    scale = 2.5
    self.status = "Open"

    self.images = {
        "Open": getAnimation("Portals/Purple/Open", 8, scale),
        "Idle": getAnimation("Portals/Purple/Idle", 8, scale),
        "Close": getAnimation("Portals/Purple/Close", 6, scale)
    }
    
  def open_portal(self, screen):
    if self.frame >= len(self.images[self.status]):
      if self.status == "Close": return
      self.frame = 0
      self.openCount += 1
      self.status = "Idle"
      if self.openCount >= self.loops: self.status = "Close"
    img = self.images[self.status][int(self.frame)]
    if self.direction == -1: img = pygame.transform.flip(img, True, False)
    screen.blit(img, (self.x, self.y))
    self.frame += self.framRate    