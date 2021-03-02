import pygame 

class SpriteSheet(object):

    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load('sprites/sprite_sheet.png')
        except pygame.error:
            print('unable to load sprite sheet: ')
            raise SystemExit

    def image_at(self, rectangle):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        color_key = image.get_at((0,0))
        image.set_colorkey(color_key)

        return image
    
    def images_at(self, rects):
        return [self.image_at(rect) for rect in rects]
    