import pygame
import random

class Potion(pygame.sprite.Sprite):
  def __init__(self, x, y, img_file):
    """
    Initializes a potion sprite
    Takes a potion, 2 integers for coordinates, and an image file
    Returns nothing
    """
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    