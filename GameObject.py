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
    
