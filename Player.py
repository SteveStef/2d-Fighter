import pygame
from Entity import Entity

class Player(Entity):
  def __init__(self,x,y,w,h,vel,health,mana,damage):
   Entity.__init__(self,x,y,w,h,vel,health,mana,damage)
   self.dash = False
   self.dashCount = 10
   self.attacking2 = False
   self.status = "Idle"
   self.frame = 0
   self.dashCount = 10
   self.isJump = False
   self.isAttacking = False
   
  def drawHitbox(self, screen):
    pygame.draw.rect(screen, "red", self.rect, 1)

  def keyboardInput(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]: self.jump()
    if keys[pygame.K_d] and not self.isAttacking: 
      self.direction.x = 1
      self.facing = 1
    elif keys[pygame.K_a] and not self.isAttacking: 
      self.direction.x = -1
      self.facing = -1
    else:
      self.direction.x = 0
      self.isAttacking = False
      self.attacking2 = False
      self.dash = False

    if keys[pygame.K_f] and self.mana > 0:
      self.isAttacking = True
      self.direction.y = 1

    if self.dash: self.activeDash(1.5)
    if keys[pygame.K_c]: self.attacking2 = True

  def activeDash(self, force):
    if self.dashCount <= 0:
      self.dash = False
      self.dashCount = 10
    else:
      self.dashCount -= 1
      self.rect.x += self.direction.x * force * self.dashCount

  def jump(self):
    if (self.direction.y == self.gravity or self.direction.y == 0):
      self.direction.y = -20
   
  def implementDash(self):
    pass
  

