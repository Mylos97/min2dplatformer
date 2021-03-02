import pygame
from GameObject import *

class Bullet(GameObject):

    def __init__(self, screen, xInput, yInput, objectID, mediator, player):
        self.screen = screen
        self.objectID = objectID
        self.mediator = mediator


        self.xInput = int(xInput/4)
        self.yInput = int(yInput/4)
        self.x_speed = 0
        self.y_speed = 0

        self.bullet_img = pygame.image.load('sprites/player/player_bullet_small.png')
        self.bullet_img.set_colorkey((253,77,211))
        self.player = player
        self.bullet_pos = player.get_player_position()
        self.bullet_pos[0] += player.get_player_scroll()
        self.bullet_pos[1] -= 4
        self.air_timer = 0
        self.bullet_bounce = 0
        self.bullet_rect = pygame.Rect(0,0,0,0)
        self.start_speed()


    def start_speed(self):
        # 128 is half of the screen 

        if self.xInput > 128:
            self.x_speed += ((self.xInput-128)/128)*4 
            self.bullet_pos[0] += 6
        else:
            self.x_speed -= ((128-self.xInput)/128)*4
            self.bullet_pos[0] -= 4


        if self.yInput > 144:
            self.y_speed = -3
        else:
            self.y_speed -= ((144-self.yInput)/144)*8
            if self.y_speed >= 6:
                self.y_speed = 6
        

    def get_bullet_rect(self):
        return self.bullet_rect
        
        
    


    def loop(self):
        
        self.y_speed += 0.25
        
        if self.y_speed > 6:
            self.y_speed = 6
        
        self.bullet_pos[1] += self.y_speed

        self.bullet_rect = pygame.Rect(self.bullet_pos[0],self.bullet_pos[1], self.bullet_img.get_width(),self.bullet_img.get_height())


        for tile in self.mediator.all_game_tiles:
            
            if self.bullet_rect.colliderect(tile) and self.air_timer > 1:
                self.bullet_pos[1] -= self.y_speed

                self.air_timer = 0
                self.bullet_bounce += 1

                if self.bullet_bounce > 1:
                    self.mediator.to_be_removed.append(self)
                
                if self.bullet_bounce == 1:
                    self.y_speed *= -1 
                    self.y_speed += 1 
                

                if self.y_speed < -12:
                    self.y_speed = -12
        
        self.bullet_pos[0] += self.x_speed
        self.air_timer += 1

        self.bullet_rect = pygame.Rect(self.bullet_pos[0],self.bullet_pos[1], self.bullet_img.get_width(),self.bullet_img.get_height())

        for tile in self.mediator.all_game_tiles:
            if self.bullet_rect.colliderect(tile) and self.air_timer > 1:
                self.bullet_pos[0] -= self.x_speed

                print("i collide")
                self.air_timer = 0
                self.x_speed *= -1
                self.bullet_bounce += 1

            if self.bullet_bounce > 1:
                    self.mediator.to_be_removed.append(self)



    def draw(self):
        self.screen.blit(self.bullet_img,(self.bullet_pos[0] - self.player.get_player_scroll() ,self.bullet_pos[1]))