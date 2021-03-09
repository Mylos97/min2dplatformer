import pygame


class Tiles(GameObject):

    def __init__(self, screen, objectID, mediator):
        self.screen = screen
        self.tile_size = 16
        self.ice_platform_left = pygame.image.load('sprites/background/platform_ice_left.png')
        self.ice_platform_middle = pygame.image.load('sprites/background/platform_ice_middle.png')
        self.ice_platform_right = pygame.image.load('sprites/background/platform_ice_right.png')
        self.ice_platform_right.set_colorkey((255,255,255))
        self.ice_platform_left.set_colorkey((255,255,255))
        self.objectID = objectID
        self.mediator = mediator
