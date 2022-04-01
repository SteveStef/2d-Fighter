import pygame

class Entity:
  def __init__(self, x, y, w, h, vel, health, mana,damage):
    self.rect = pygame.Rect(x,y,w,h)
    self.direction = pygame.math.Vector2(0,0) # x, y
    self.gravity = 1.9
    self.vel = vel
    self.maxVel = vel
    self.facing = -1
    self.hitWall = False
    self.jCount = 0
    self.health = health
    self.mana = mana
    self.fullHealth = health
    self.fullMana = mana
    self.dmg = damage
    self.isDead = False
    self.knockCount = 10
    self.isKnocked = False

  def drawHitbox(self, screen):
    pygame.draw.rect(screen, "red", self.rect, 1)

  def knockback(self, knock, d):
    if self.knockCount > 0:
      self.knockCount -= 1
      pos = self.rect.x + knock * self.knockCount * d
      if pos > 0 and pos < 3000: self.rect.x += knock * self.knockCount * d
    else:
      self.knockCount = 10
      self.isKnocked = False

  def applyGravity(self):
    self.direction.y += self.gravity
    self.rect.y += self.direction.y
  
  def move(self):
    self.rect.x += self.direction.x * self.vel

  def drawHealthBars(self, screen, h):
     #the health bar is shifting to the right as it lowers
    displayHealth = h * (self.health / self.fullHealth)
    rect = pygame.Rect((self.rect.midbottom[0] - h / 2.5)-5, self.rect.y - 20, h, 6)
    rect2 = pygame.Rect((self.rect.midbottom[0] - h / 2.5)-5, self.rect.y - 20, displayHealth, 6)
    pygame.draw.rect(screen, "#DC143C", rect)
    pygame.draw.rect(screen, "#7FFF00", rect2)

  def drawManaBars(self, screen, h):
    displayHealth = h * (self.mana / self.fullMana)
    rect = pygame.Rect((self.rect.midbottom[0] - h / 2.5)-5, self.rect.y-23, displayHealth,3)
    pygame.draw.rect(screen, "#00CDCD", rect)