import pygame
from Tiles import Tile
from Settings import *

class Level:
  def __init__(self, data):
    self.data = data
    self.tiles = []
    self.createLevel()
    self.world_scroll = 0
  
  def createLevel(self):
    for i in range(len(self.data)):
      for j in range(len(self.data[i])):
        if len(self.data[i][j]) > 0:
          x = j * TILE_SIZE
          y = i * TILE_SIZE
          if self.data[i][j] != "-1":
            path = "Level Tiles/"+self.data[i][j]+".png"
            self.tiles.append(Tile((x,y), TILE_SIZE, path))

  def draw_map(self, screen, player, entityList, pets):
    for tile in self.tiles:
      tile.draw(screen)
      tile.update(self.world_scroll)
    self.handle_pet(screen, player, pets)
    self.handle_entities(screen, player, entityList)
    self.handle_player(screen, player, entityList)

# ======================================= HANDLING PLAYER/PET/ENTITY ===================================== #
  def handle_entities(self, screen, player, entityList):
    for entity in entityList:
      if not entity.isDead:
        entity.world_shift(self.world_scroll)
        entity.update(screen, player)
        self.tile_collision_x(entity)
        self.tile_collision_y(entity) # applies gravity already
      else:
        if entity.isDead: entityList.remove(entity)

  def handle_player(self, screen, player, entityList):
    player.update(screen, entityList)
    self.scroll_x(player)
    self.bullet_tile_collision(player)
    self.bullet_entity_collision(screen, player, entityList)
    self.tile_collision_x(player)
    self.tile_collision_y(player)
    
  def handle_pet(self, screen, player, pets):
    for pet in pets:
      pet.world_shift(self.world_scroll)
      pet.update(screen, player)
      self.tile_collision_x(pet)
      self.tile_collision_y(pet)

# ============================================= COLLISION ========================================== #
  def bullet_entity_collision(self, screen, player, entityList): # bullets hitting entities
    for bullet in player.bullets:
      for entity in entityList:
        if bullet.rect.colliderect(entity.rect):
          # dmg to entity
          entity.damage(player.dmg)
          bullet.impacting = True
          if bullet.dead:
            player.bullets.remove(bullet)
          break

  def bullet_tile_collision(self, player): # bullets hitting tiles
    for bullet in player.bullets:
      for tile in self.tiles:
        if bullet.rect.colliderect(tile.rect):
          bullet.impacting = True
          if bullet.dead: player.bullets.remove(bullet)
          break

  def tile_collision_x(self, entity): # entity hitting tiles on x
     entity.move()
     for tile in self.tiles:
        if entity.rect.colliderect(tile.rect):
           entity.hitWall = True
           if entity.direction.x < 0:
              entity.rect.left = tile.rect.right
           elif entity.direction.x > 0:
              entity.rect.right = tile.rect.left

  def tile_collision_y(self, entity): # entity hitting tiles on y
    entity.applyGravity()
    for tile in self.tiles:
      if entity.rect.colliderect(tile.rect):
        if entity.direction.y > 0: # downwards
          entity.rect.bottom = tile.rect.top
          entity.direction.y = 0
        elif entity.direction.y < 0: # upwards
          entity.rect.top = tile.rect.bottom
          entity.direction.y = 1
# ============================================= WORLD SCROLLFOR PLAYER ========================================== #

  def scroll_x(self, player):
    player_x = player.rect.centerx
    direction_x = player.direction.x
    # window scrolling logic
    if player_x < WIDTH/4 and direction_x < 0: # moving to left
      self.world_scroll = player.maxVel
      if player.dash: self.world_scroll = 12
      player.vel = 0
    elif player_x > WIDTH - (WIDTH/4) and direction_x > 0: # moving right
      self.world_scroll = -player.maxVel
      if player.dash: self.world_scroll = -12
      player.vel = 0
    else:
      self.world_scroll = 0
      player.vel = player.maxVel