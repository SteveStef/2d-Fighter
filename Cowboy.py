

import pygame
from Player import Player
from Images import getAnimation
from Projectile import Projectile, Slash

class Cowboy(Player):
  def __init__(self, x, y, w, h, vel, health, mana, damage):
    Player.__init__(self, x, y, w, h, vel, health, mana, damage)
    self.slash = Slash(x,y)
    self.bullets = []
    scale = 2.5

    self.images = {
      "Idle": getAnimation("Characters/Cowboy/Idle", 7, scale),
      "Move": getAnimation("Characters/Cowboy/Move", 8, scale),
      "Shoot": getAnimation("Characters/Cowboy/Shoot", 4, scale),
      "Whip": getAnimation("Characters/Cowboy/Whip", 8, scale),
      "Roll": getAnimation("Characters/Cowboy/Roll", 7, scale),
      "Death": getAnimation("Characters/Cowboy/Death", 5, scale)
    }

    self.offsets = {
      "Idle": (-20, -9),
      "Move": (-65, -15),
      "Shoot": (-60, -15),
      "Whip": (-60, -30),
      "Roll": (-60, 0)
    }

    self.frameRates = {
      "Idle": 0.2,
      "Move": 0.3,
      "Shoot": 0.3,
      "Whip":  0.4,
      "Roll": 0.6,
    }


  def animate(self, screen):
    self.getStatus()
    if self.frame >= len(self.images[self.status]): self.frame = 0
    img = self.images[self.status][int(self.frame)]
    if self.facing == -1: img = pygame.transform.flip(img, True, False)
    offX = self.offsets[self.status][0]
    offY = self.offsets[self.status][1]
    if self.status == "Shoot": 
      offX = self.shoot_offset(offX)
      if self.frame >= 2 and self.frame < 2 + self.frameRates["Shoot"]: self.shoot()
    screen.blit(img, (self.rect.x + offX, self.rect.y+ offY))
    self.frame += self.frameRates[self.status]


  def shoot(self):
    bullet = Projectile(self.rect.x + 15 * self.facing, self.rect.y+6, 20, self.facing)
    self.mana -= 1
    self.bullets.append(bullet)


  def drawBullets(self, screen):
    for bullet in self.bullets:
      bullet.update(screen)


  def shoot_offset(self, offX):
    if self.frame >= 3: return offX - 15 * self.facing
    elif self.frame >= 2: return offX - 10 * self.facing
    elif self.frame >= 1: return offX - 5 * self.facing
    else: return offX
      
  def getStatus(self):
    if self.dash: self.status = "Roll"
    elif self.direction.x != 0: self.status = "Move"
    elif self.isAttacking: self.status = "Shoot"
    elif self.attacking2: self.status = "Whip"
    else: self.status = "Idle"


  def attack(self, screen, entityList):
    for entity in entityList:
      if abs(self.rect.centerx - entity.rect.centerx) < 150:
        if abs(self.rect.y - entity.rect.y) <70:
          if self.facing != entity.facing and self.attacking2 and self.status == "Whip" and self.frame >= 2 and self.frame < 2.5:
            self.slash.updatePos(entity.rect.centerx, entity.rect.centery)
            entity.damage(self.dmg*2)
            # enemy knockback
            self.slash.active = True
            self.mana += 1
            if self.mana >= self.fullMana: self.mana = self.fullMana


  def update(self, screen, entityList):
    self.attack(screen, entityList)
    self.keyboardInput()
    self.animate(screen)
    self.slash.animate(screen)
    self.move()
    self.drawBullets(screen)
    self.drawHealthBars(screen,50)
    self.drawManaBars(screen,50)