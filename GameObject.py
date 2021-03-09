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
    
