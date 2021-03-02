import pygame, sys

from pygame.locals import *
from Player import *
from Mediator import *
from GameMap import *
pygame.init()

WINDOW_SIZE = (1024,768)
clock = pygame.time.Clock()


screen = pygame.display.set_mode(WINDOW_SIZE,0,32)
display = pygame.Surface((256,192))

mediator = Mediator()
player = Player(display,'player',mediator)
mediator.all_game_entities.append(player)
gameMap = GameMap(display,'tiles',mediator,player)



while True:
    display.fill((57, 138, 215))
    mediator.all_game_tiles.clear()
    gameMap.draw_map()

    for object in mediator.all_game_entities:
        object.loop()
        object.draw()
    

    mediator.all_game_entities = [object for object in mediator.all_game_entities if object not in mediator.to_be_removed]

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    

    surf = pygame.transform.scale(display, WINDOW_SIZE)
    screen.blit(surf, (0,0))
    pygame.display.update()
    clock.tick(60)
