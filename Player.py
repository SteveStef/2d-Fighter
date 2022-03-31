import pygame
from Entity import Entity

class Player(Entity):
  def __init__(self,x,y,w,h,vel,health,mana,damage):
   Entity.__init__(self,x,y,w,h,vel,health,mana,damage)
   self.dash = False
   self.attacking2 = False
   self.status = "Idle"
   self.frame = 0
  def drawHitbox(self, screen):
    pygame.draw.rect(screen, "red", self.rect, 1)

  def keyboardInput(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]: self.jump()
    if keys[pygame.K_d]: 
      self.direction.x = 1
      self.facing = 1
    elif keys[pygame.K_a]: 
      self.direction.x = -1
      self.facing = -1
    else:
      self.direction.x = 0
      self.isAttacking = False
      self.attacking2 = False
      self.dash = False

    if keys[pygame.K_f] and self.mana > 0: self.isAttacking = True
    if keys[pygame.K_LSHIFT]: self.attacking2 = True
    if keys[pygame.K_LCTRL]: self.dash = True

  def jump(self):
    if self.direction.y == self.gravity or self.direction.y == 0: self.direction.y = -22
   
  def implementDash(self):
    pass
  

