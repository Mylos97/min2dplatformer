import pygame

class HUD:

    def __init__(self, screen, player):
        self.screen = screen 
        self.player = player
        self.font = pygame.font.Font('font/kongtext.ttf', 8)
        self.world = 1
        self.level = 1
        self.score = 0


    def draw_overlay(self):
        self.levels = self.font.render(str(self.world) + ":" + str(self.level),0,(255,255,255))
        self.score_display = self.font.render("Score:" + str(self.score) , 0 ,(255,255,255))
        self.screen.blit(self.levels,(216,8))
        self.screen.blit(self.score_display,(8,8))
    

