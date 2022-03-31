import pygame
import os

imageTitles = [
  "tile000.png","tile001.png","tile002.png","tile003.png","tile004.png",
  "tile005.png","tile006.png","tile007.png","tile008.png","tile009.png",
  "tile010.png","tile011.png","tile012.png","tile013.png","tile014.png",
  "tile015.png","tile016.png","tile017.png","tile018.png","tile019.png",
  "tile020.png","tile021.png","tile022.png","tile023.png","tile024.png",
]

def getAnimation(path, frames, scale):
  animationList = []
  for i in range(frames):
    img = pygame.image.load(os.path.join(path,imageTitles[i])).convert_alpha()
    img = pygame.transform.scale(img,(int(img.get_width()*scale),int(img.get_height()*scale)))
    animationList.append(img)
  return animationList