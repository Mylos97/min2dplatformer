import pygame, sys
from GameObject import * 
from Mediator import *
from Player import *
from Enemy import *

class GameMap(GameObject):
    
    def __init__(self, screen, objectID, mediator, player):
        self.screen = screen
        self.map = self.load_map('map.txt')
        self.tile_size = 16
        self.ice_platform_left = pygame.image.load('sprites/background/platform_ice_left.png')
        self.ice_platform_middle = pygame.image.load('sprites/background/platform_ice_middle.png')
        self.ice_platform_right = pygame.image.load('sprites/background/platform_ice_right.png')
        self.ice_platform_right.set_colorkey((255,255,255))
        self.ice_platform_left.set_colorkey((255,255,255))
        self.objectID = objectID
        self.mediator = mediator
        self.player = player
        self.load_enemy()


    def load_map(self, path):
        f = open(path,'r') 
        data = f.read()
        data = data.split('\n')
        game_map = []

        for row in data:
            game_map.append(list(row))
        
        return game_map
    
    def load_enemy(self):
        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[0])): 
                if self.map[i][j] == 'E':
                    self.mediator.all_game_entities.append(Enemy(self.screen,j*self.tile_size,i*self.tile_size, 'enemy', self.mediator, self.player))

    ## Add player scroll
    def draw_map(self):
        

        for i in range(0,len(self.map)):
            for j in range(0,len(self.map[0])): 
                if self.map[i][j] == '1':
                    self.screen.blit(self.ice_platform_middle, (j * self.tile_size - self.player.get_player_scroll(), i * self.tile_size))
                if self.map[i][j] == '2':
                    self.screen.blit(self.ice_platform_left,(j * self.tile_size - self.player.get_player_scroll(), i * self.tile_size))
                if self.map[i][j] == '3':
                    self.screen.blit(self.ice_platform_right,(j * self.tile_size - self.player.get_player_scroll(), i * self.tile_size))

                if self.map[i][j] != '0' and self.map[i][j] != 'E':
                    self.mediator.all_game_tiles.append(pygame.Rect(j * self.tile_size , i * self.tile_size, self.tile_size, self.tile_size))
    

    def loop(self):
        pass
    def draw(self):
        pass