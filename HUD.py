import pygame

class HUD:

    def __init__(self, screen, player):
        self.screen = screen 
        self.player = player
        self.font = pygame.font.Font('font/kongtext.ttf', 8)
        self.world = 1
        self.level = 1


    def draw_overlay(self):
        self.levels = self.font.render(str(self.world) + ":" + str(self.level),0,(255,255,255))
        
        self.screen.blit(self.levels,(216,8))
    

