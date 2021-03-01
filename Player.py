import pygame, sys
from GameObject import *
from Bullet import *

class Player(GameObject):

    def __init__(self, screen, objectID, mediator):
        self.screen = screen
        self.objectID = objectID
        self.mediator = mediator

        self.player_image = pygame.image.load('sprites/player/player_mock_img.png')
        self.player_image.set_colorkey((253,77,211))
        self.player_location = [100,100]
        self.player_speed_x = 4
        self.player_speed_y = 0
        self.player_movement = [0,0]
        self.player_rect = pygame.Rect(self.player_location[0],self.player_location[1],self.player_image.get_width(),self.player_image.get_height())
        self.air_timer = 0
        self.moving_right = False
        self.moving_left = False
        self.player_scroll = 0
        self.shooting_cooldown = 0


    
    def update_player_scroll(self):
        self.player_scroll += (player_rect.x -player_scroll - 112)/10
        self.player_scroll = int(player_scroll)
    

    def loop(self):
        self.player_movement = [0,0]

        self.player_scroll += (self.player_rect.x -self.player_scroll - 112)/4
        self.player_scroll = int(self.player_scroll)

        self.shooting_cooldown += 1

        if self.moving_right == True:
            self.player_movement[0] += 2
        if self.moving_left == True:
            self.player_movement[0] -= 2
        


        self.player_movement[1] += self.player_speed_y
        self.player_speed_y += 0.2
        
        if self.player_speed_y > 6:
            self.player_speed_y = 6


        self.player_rect, collions = self.move(self.player_rect, self.player_movement, self.mediator.all_game_tiles)

        if collions['bottom']:
            self.player_speed_y = 0
            self.air_timer = 0
        else:
            self.air_timer += 1
    
        if collions['top']:
            self.player_speed_y = 0.2

        

        self.player_input()

    def loopv2(self):
        self.player_movement = [0,0]

        if self.moving_right == True:
            self.player_movement[0] += 2
        if self.moving_left == True:
            self.player_movement[0] -= 2
        
        self.player_movement[1] += self.player_speed_y
        self.player_speed_y += 0.2

        if self.player_speed_y > 6:
            self.player_speed_y = 6
        
        self.player_rect, collions = self.move(self.player_rect,self.player_movement, self.mediator.all_game_tiles)

        if collions['bottom']:
            self.player_speed_y = 0
            self.air_timer = 0
        else:
            self.air_timer += 1
    
        if collions['top']:
            self.player_speed_y = 0.2
        
        self.player_scroll += (self.player_rect.x - self.player_scroll - 96)
        self.player_scroll = int(self.player_scroll)

        self.player_input()

   
    def get_player_scroll(self):
        return self.player_scroll
    
    def get_player_position(self):
            self.playerPos = [self.player_rect.x  - self.player_scroll,self.player_rect.y]
            return self.playerPos

    def draw(self):
        self.screen.blit(self.player_image,((self.player_rect.x - self.player_scroll), self.player_rect.y))
    

    def collision_test(self):
        hit_list = []
        for tile in self.mediator.all_game_tiles:
            if self.player_rect.colliderect(tile):
                hit_list.append(tile)

        return hit_list

    def move(self, rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}


        rect.x += movement[0]
        hit_list = self.collision_test()

        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            if movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        
        rect.y += movement[1]
        hit_list = self.collision_test()

        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            if movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True

        return rect, collision_types
    
    def player_input(self):
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
        
        if mouse[0] == True and self.shooting_cooldown > 30:
            self.shooting_cooldown = 0
            self.mousePos = pygame.mouse.get_pos()
            self.mediator.all_game_entities.append(Bullet(self.screen, self.mousePos[0], self.mousePos[1],'f_bullet', self.mediator, self))

        if keystate[pygame.K_w]:
            if self.air_timer < 6:
                    self.player_speed_y = -5
        
        if keystate[pygame.K_ESCAPE]:
            sys.exit()
        
        