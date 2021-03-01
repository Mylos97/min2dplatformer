import pygame
from GameObject import *

class Bullet(GameObject):

    def __init__(self, screen, xInput, yInput, objectID, mediator, player):
        self.screen = screen
        self.xInput = int(xInput/4)
        self.yInput = int(yInput/4)
        self.x_speed = 0
        self.y_speed = 0
        self.objectID = objectID
        self.mediator = mediator
        self.bullet_img = pygame.image.load('sprites/player/player_bullet_small.png')
        self.bullet_img.set_colorkey((253,77,211))
        self.player = player
        self.bullet_pos = player.get_player_position()
        self.start_speed()


    def start_speed(self):
        # 128 is half of the screen 

        if self.xInput > 128:
            self.x_speed += (self.xInput/128)*2 
        else:
            print("hello")
            self.x_speed -= ((128-self.xInput)/128)*4



        
        if self.yInput > 144:
            self.y_speed = -3
        else:
            self.y_speed -= ((144-self.yInput)/144)*8
            if self.y_speed >= 6:
                self.y_speed = 6




    def loop(self):


        self.bullet_pos[0] += self.x_speed


        self.y_speed += 0.2
        
        if self.y_speed > 6:
            self.y_speed = 6
        
        self.bullet_pos[1] += self.y_speed


    def draw(self):
        self.screen.blit(self.bullet_img,(self.bullet_pos[0],self.bullet_pos[1]))