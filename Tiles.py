import pygame

class Tile:
  def __init__(self, pos, size, path):
    self.image = pygame.image.load(path).convert_alpha()
    self.rect = self.image.get_rect(topleft = pos)
  
  def update(self, x_shift):
    self.rect.x += x_shift
  
  def draw(self, screen):
    screen.blit(self.image, self.rect)