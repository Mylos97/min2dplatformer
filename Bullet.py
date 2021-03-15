import pygame
from GameObject import *
from SpriteSheet import *


class Bullet(GameObject):

    def __init__(self, screen, xInput, yInput, objectID, mediator, player):
        self.screen = screen
        self.objectID = objectID
        self.mediator = mediator


        self.xInput = int(xInput/4)
        self.yInput = int(yInput/4)
        self.bullet_speed = [0,0]


        self.ss = SpriteSheet('sprites/sprite_sheet.png')
        self.bullet_img = self.ss.image_at(pygame.Rect(130,286,8,8))
        self.bullet_img.set_colorkey((253,77,211))
        
        
        self.player = player
        self.bullet_pos = player.get_player_position()
        self.bullet_pos[0] += player.get_player_scroll()
        self.bullet_pos[1] -= 4
        self.air_timer = 0
        self.bullet_bounce = 0
        self.bullet_rect = pygame.Rect(self.bullet_pos[0],self.bullet_pos[1], self.bullet_img.get_width(),self.bullet_img.get_height())
        self.start_speed()


    def start_speed(self):
        # 128 is half of the screen 

        if self.xInput > 128:
            self.bullet_speed[0] += ((self.xInput-128)/128)*4 
            self.bullet_pos[0] += 6
        else:
            self.bullet_speed[0] -= ((128-self.xInput)/128)*4
            self.bullet_pos[0] -= 4


        if self.yInput > 144:
            self.bullet_speed[1] = -3
        else:
            self.bullet_speed[1] -= ((144-self.yInput)/144)*8
            if self.bullet_speed[1] >= 6:
                self.bullet_speed[1] = 6
        

    def get_rect(self):
        return self.bullet_rect
        

    def loop(self):
        self.bullet_speed[1] += 0.2


        self.bullet_rect, collions = self.object_check_collision_tiles(self.bullet_rect, self.bullet_speed)

        if collions['left'] or collions['right']:
            self.bullet_speed[0] *= -0.5
            self.bullet_bounce += 1


        if collions['top'] or collions['bottom']:
            self.bullet_speed[1] *= -0.5
            self.bullet_bounce += 1

        if self.bullet_bounce > 2:
            self.bullet_img = self.ss.image_at(pygame.Rect(146,286,8,8))
            self.mediator.to_be_removed.append(self)
        
        if self.bullet_rect.y > 250:
            self.mediator.to_be_removed.append(self)


    def draw(self):
        self.screen.blit(self.bullet_img,(self.bullet_rect.x - self.player.get_player_scroll() ,self.bullet_rect.y))