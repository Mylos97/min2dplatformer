class GameObject:

    def __init__(self, objectID, mediator):
        self.objectID = objectID
        self.mediator = mediator

    def draw(self):
        pass

    def loop(self):
        pass

    def getObjectID(self):
        return self.objectID

    def get_damage(self):
        pass
    
    def get_rect(self):
        pass
    

    def object_check_collision_tiles(self, rect, movement):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}


        rect.x += movement[0]
        hit_list = self.get_collision_tiles(rect)

        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            if movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        
        rect.y += movement[1]
        hit_list = self.get_collision_tiles(rect)

        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            if movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True

        return rect, collision_types

    def get_collision_tiles(self, rect):
        hit_list = []
        for tile in self.mediator.all_game_tiles:
            if rect.colliderect(tile):
                hit_list.append(tile)

        return hit_list

    def check_boundary(self, rect):
        for tile in self.mediator.all_boundry_tiles:
            if rect.colliderect(tile):
                return True
    


    def on_screen(self, rect , player):
        if rect.x - player.get_player_scroll() > - 16 and rect.x - player.get_player_scroll() < 256:
            return True

        return False

    def get_collision_bullet(self, rect):

        for object in self.mediator.all_game_entities:
                if object.getObjectID() == 'f_bullet':
                    if rect.colliderect(object.get_rect()):
                        self.mediator.to_be_removed.append(object)
                        return True

        return False

    def get_collision_entities(self, rect, ID):
        for object in self.mediator.all_game_entities:
            if object.getObjectID() == ID:
                if rect.colliderect(object.get_rect()):
                    return True

        return False