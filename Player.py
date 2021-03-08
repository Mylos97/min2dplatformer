import pygame, sys
from GameObject import *
from Bullet import *
from SpriteSheet import *


class Player(GameObject):


    def __init__(self, screen, objectID, mediator):
        self.screen = screen
        self.objectID = objectID
        self.mediator = mediator
        
        self.ss = SpriteSheet('sprites/sprite_sheet.png')


        self.player_image = self.ss.image_at(pygame.Rect(20,147,9,13))
        self.player_image.set_colorkey((253,77,211))
        self.player_showing_image = self.player_image

        self.player_rects_jump = [pygame.Rect(17, 194,14,13), pygame.Rect(35, 194,11,13)]
        self.player_images_jump = self.ss.images_at(self.player_rects_jump)

        self.player_rects_moving = [pygame.Rect(20,147,9,13),pygame.Rect(35,146,11,13),pygame.Rect(52,147,9,13)]
        self.player_images_moving = self.ss.images_at(self.player_rects_moving)
        self.animation_timer_moving_right = 0
        self.animation_timer_moving_int_right = 0

        self.animation_timer_moving_left = 0
        self.animation_timer_moving_int_left = 0



        self.player_location = [100,100]
        self.player_speed_x = 4
        self.player_speed_y = 0
        self.player_movement = [0,0]
        self.player_rect = pygame.Rect(self.player_location[0],self.player_location[1],self.player_image.get_width(),self.player_image.get_height())
        
        self.air_timer = 0
        self.idle_timer = 0
        self.moving_right = False
        self.moving_left = False
        self.last_direction = ''


        self.player_scroll = 0
        self.shooting_cooldown = 0




    def loop(self):
        self.idle_timer += 1
        self.player_movement = [0,0]


        
        self.shooting_cooldown += 1

        ## x movement ##
        if self.moving_right == True:
            self.idle_timer = 0
            self.player_movement[0] += 2
            self.last_direction = 'right'
        if self.moving_left == True:
            self.idle_timer = 0
            self.player_movement[0] -= 2
            self.last_direction = 'left'
        
        self.player_rect, collions = self.object_check_collision_tiles(self.player_rect, self.player_movement)

        self.player_movement = [0,0]


        ## y movement ##
        self.player_movement[1] += self.player_speed_y
        self.player_speed_y += 0.2
        
        if self.player_speed_y > 6:
            self.player_speed_y = 6


        ## Collion function ##
        self.player_rect, collions = self.object_check_collision_tiles(self.player_rect, self.player_movement)

        ## Check for collions bottom ##
        if collions['bottom']:
            self.player_speed_y = 0
            self.air_timer = 0
        else:
            self.idle_timer = 0
            self.air_timer += 1

    
        ## Check for hitting head ##
        if collions['top']:
            self.player_speed_y = 0.2

        
        ## Player scroll must be used in almost all classes ##
        self.player_scroll += (self.player_rect.x -self.player_scroll - 128)
        self.player_scroll = int(self.player_scroll)


        ## Moving right animation ##
        if self.moving_right == True and self.air_timer < 6:
            self.animation_timer_moving_right += 1

            self.animation_timer_moving_right %= 6

            if self.animation_timer_moving_right%6 == 0:
                self.animation_timer_moving_int_right += 1

                if self.animation_timer_moving_int_right > 2:
                    self.animation_timer_moving_int_right = 0

            
            self.player_showing_image = self.player_images_moving[self.animation_timer_moving_int_right]   
        
        ## Moving left animations ##
        if self.moving_left == True and self.air_timer < 6:
            self.animation_timer_moving_left += 1

            self.animation_timer_moving_left %= 6

            if self.animation_timer_moving_left%6 == 0:
                self.animation_timer_moving_int_left += 1

                if self.animation_timer_moving_int_left > 2:
                    self.animation_timer_moving_int_left = 0
            self.player_showing_image = pygame.transform.flip(self.player_images_moving[self.animation_timer_moving_int_left],True,False)


        ## Falling Down Left and Right ##
        if self.player_speed_y > 2.5 and self.moving_right:
            self.idle_timer = 0
            self.player_showing_image = self.player_images_jump[1]

        if self.player_speed_y > 2.5 and self.moving_left:
            self.idle_timer = 0
            self.player_showing_image =  pygame.transform.flip(self.player_images_jump[1],True,False)


        ## Player stop image left and right
        if self.last_direction == 'right' and self.idle_timer > 2:
            self.player_showing_image = self.player_image
        elif self.last_direction == 'left' and self.idle_timer > 2:
            self.player_showing_image = pygame.transform.flip(self.player_image,True,False)


        ## Player jump left and right 
        
        if self.moving_right and self.player_speed_y < 0:
            self.player_showing_image = self.player_images_jump[0]
        elif self.moving_left and self.player_speed_y < 0:
            self.player_showing_image = pygame.transform.flip(self.player_images_jump[0],True,False)

        self.player_input()




    def get_player_scroll(self):
        return self.player_scroll
    
    def get_player_position(self):
            self.playerPos = [self.player_rect.x  - self.player_scroll,self.player_rect.y]
            return self.playerPos

    def draw(self):
        self.screen.blit(self.player_showing_image,((self.player_rect.x - self.player_scroll), self.player_rect.y))
    

    
    def player_input(self):

        ## Move left or right ##
        self.player_speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.moving_left = True
        else:
            self.moving_left = False
        if keystate[pygame.K_d]:
            self.moving_right = True
        else:
            self.moving_right = False
        mouse = pygame.mouse.get_pressed()
        

        ## Shooting ##
        if mouse[0] == True and self.shooting_cooldown > 4:
            self.shooting_cooldown = 0
            self.mousePos = pygame.mouse.get_pos()
            print(self.mousePos)
            self.mediator.all_game_entities.append(Bullet(self.screen, self.mousePos[0], self.mousePos[1],'f_bullet', self.mediator, self))

        ## Jump with animation left and right
        if keystate[pygame.K_w]:
            if self.air_timer < 6:
                    self.player_speed_y = -5
                    


        
        if keystate[pygame.K_SPACE]:
            self.player_speed_y -= 1
            if self.player_speed_y < -2:
                self.player_speed_y = -2

        if keystate[pygame.K_ESCAPE]:
            sys.exit()
        
        